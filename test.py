import nltk
from nltk.corpus import brown
from my_corpus import MyCorpus as mc



lib=mc()
print("bo" in lib.wordList)
# lib.wordList.clear()
lib.bigrams.clear()

def isWord(word):
        if(len(word)==1):
                if(word!="a"): return False
        for char in word:
                if not char.isalpha(): return False
        return True

cats=brown.categories()

res=set()

for doc_name in cats:
        data=list(w.lower() for w in set(brown.words(categories=doc_name)))

        pairs=list()
        it=iter(data)
        for i in range(1, len(data)):
                if data[i-1] not in mc.wordList: continue
                if data[i] not in mc.wordList: continue
                res.add((data[i-1], data[i]))


        # fdist=nltk.FreqDist([w.lower() for w in data if isWord(w.lower())])
        # for key in fdist.keys():
        #         if(fdist[key]<2): continue
        #         res.add(key)
        # for key, data in fdist[:100]:
        #         print(key, data)
        # print(len(fdist))

print(len(res))

for word in res:
        lib.addBigram(word)

lib.saveBigrams()