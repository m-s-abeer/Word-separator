from my_corpus import MyCorpus as mc
from ahocorapy import KeywordTree as AhoCora

lib = mc()
aho = AhoCora(case_insensitive=True)

def buildTrie():
    for word in lib.wordList:
        aho.add(str(word))
    aho.finalize()

buildTrie()

def bigramMatch(res):
    cnt=int(0)
    for i in range(1, len(res)):
        if((res[i-1], res[i]) in lib.bigrams):
            cnt+=1
    return cnt

def bruteForce(qText, word_starts, pos: int, strt: int, len: int, res):
    if pos==len: #Base Case
        # store(res)
        print("Result: ", res, bigramMatch(res))
        return None

    for i in range(pos, len):
        for val in word_starts[i]:
            tmp=res.copy()
            if i>strt:
                tmp.append(qText[strt:i])
            tmp.append(qText[i:i+val])
            bruteForce(qText, word_starts, i+val, i+val, len, tmp)
        return None


### Gets query text and returns word tokens
def query(qText=""):
    qText+="." #ending indicator
    qText=qText.lower()
    # print(qText)
    ### Run aho-corasick and generate lists of possible words in each end-points
    all_result=aho.search_all(qText) # gets the list of all possible dictionary words in format(word, start_pos)
    qLen=len(qText)
    word_starts=[[] for i in range (0, qLen)] # list of possible word length from each position
    word_starts[-1].append(int(1))

    for val, pos in all_result:
        # print(val, pos, len(val))
        word_starts[pos].append(int(len(val)))
    
    ### Call brute-force for smaller sentences
    bruteForce(qText, word_starts, int(0), int(0), int(qLen), [])

    ### Try randomized algorithm for larger sentences

# take queries
while(True):
    qText=str(input("Enter your query sentence: "))
    print('Your query: "' + qText + '"')
    query(str(qText))
