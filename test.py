from my_corpus import MyCorpus as mc
from ahocorapy import KeywordTree as AhoCora

lib = mc()
aho = AhoCora(case_insensitive=True)

def buildTrie():
    for word in lib.wordList:
        aho.add(str(word))
    aho.finalize()

buildTrie()

results = aho.search_all("myname")
for result in results:
    print(result)

qText=str(input("Enter your query sentence: "))
print('Your query: "' + qText + '"')
# query(str(qText))
all_result=aho.search_all(qText)
for xx in all_result:
    print(xx)
    