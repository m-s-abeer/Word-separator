import nltk
from nltk.corpus import brown
from my_corpus import MyCorpus as mc

lib=mc()
# lib.wordList.clear()

def isWord(word):
        if(len(word)==1):
                if(word!="a"): return False
        for char in word:
                if not char.isalpha(): return False
        return True

cats=brown.categories()

res=set()

for doc_name in cats:
        data=brown.words(categories=doc_name)
        fdist=nltk.FreqDist([w.lower() for w in data if isWord(w.lower())])
        for key in fdist.keys():
                if(fdist[key]<2): continue
                res.add(key)
        # for key, data in fdist[:100]:
        #         print(key, data)
        # print(len(fdist))

print(len(res))

for word in res:
        lib.addWord(word)

lib.saveWordList()
