from my_corpus import MyCorpus as mc
from ahocorapy import KeywordTree as AhoCora
import datetime
lib = mc()
aho = AhoCora(case_insensitive=True)

def buildTrie():
    for word in lib.wordList:
        aho.add(str(word))
    aho.finalize()

buildTrie()
print("Aho-Corasick finalized")

def bigramScore(res, bigram_score=int(3), word_found=int(-2), word_not_found=int(-3)):
    if res[0]: cnt= word_found if res[0] in lib.wordList else word_not_found
    else: cnt=int(0)
    for i in range(1, len(res)):
        if((res[i-1], res[i]) in lib.bigrams):
            cnt+=bigram_score
        # elif res[i] in lib.wordList:
        #     cnt+=1
        if res[i] not in lib.wordList:
            cnt+=word_not_found
        else:
            cnt+=word_found
    return cnt

results=set()
global max_score

def storeResult(score, line):
    global max_score
    if score+8>=max_score:
        max_score=max(max_score, score)
        results.add((score, tuple(line)))

def countChar(line):
    ans=int(0)
    for word in line:
        ans+=len(word)+int(1)
    return ans

def printResult():
    if not results: return [[int(0)], "No results found"]
    mn=min([sc[0] for sc in results])
    res=[ [items[0]-mn+1, (" ").join(list(items[1]))] for items in list(results)]
    res.sort(key=lambda x: (-x[0], x[1].count(' ')))
    return res
    # print(res)
    # max_len=int(max(countChar(sc[1]) for sc in res))
    # for score, line in res:
    #     print("{:{x}} [Score: {}]".format(str((" ").join(line)), score-mn+1, x=max_len))
    #     # print((" ").join(line), "[ Score -> ", score-mn+1, "]")

def bruteForce(qText, word_starts, pos: int, len: int, res, next_words=2):
    if pos==len: #Base Case
        storeResult(bigramScore(res), res)
        # print("Result: ", res, bigramScore(res))
        return None
    for i in range(pos, min(pos+9, len)):
        if not word_starts[i]:
            continue
        for val in word_starts[i]:
            tmp=res.copy()
            if i>pos:
                tmp.append(qText[pos:i])
            tmp.append(qText[i:i+val])
            # print(tmp, "from", i, val)
            bruteForce(qText, word_starts, i+val, len, tmp)
        next_words-=1
        if not next_words:
            return None


def normalize(qText):
    ans=str()
    for x in qText:
        if x.isalpha():
            ans=ans+x.lower()
    return ans

### Gets query text and returns word tokens
def query(qText=""):
    print("Query taken at:", datetime.datetime.now())
    qText.replace('.', '')
    global max_score
    max_score=-int(100000000)
    qText=normalize(qText)#qText.replace(" ", "").lower()
    qText+="." #ending indicator
    results.clear()
    # print(qText)
    ### Run aho-corasick and generate lists of possible words in each end-points
    all_result=aho.search_all(qText) # gets the list of all possible dictionary words in format(word, start_pos)
    qLen=len(qText)
    word_starts=[[] for i in range (0, qLen)] # list of possible word length from each position
    word_starts[-1].append(int(1))

    for val, pos in all_result:
        # print(val, pos, len(val))
        word_starts[pos].append(int(len(val)))
    for item in word_starts:
        item.sort(reverse=True)

    print("Word starts generated")
    # print(all_result)
    print(word_starts)
    # print(qLen)
    ### Call brute-force for smaller sentences
    bruteForce(qText, word_starts, int(0), int(qLen), [], next_words=3)
    
    print("Results generated at:", datetime.datetime.now())
    return printResult()
    ### Try randomized algorithm for larger sentences

# take queries
# while(True):
#     qText=str(input("Enter your query sentence: "))
#     print('Your query: "' + qText + '"')
#     query(str(qText))
