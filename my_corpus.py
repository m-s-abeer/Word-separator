import os

class MyCorpus:
    wordListPath=os.path.abspath("my_corpus/wordList.txt")
    bigramPath=os.path.abspath("my_corpus/bigrams.txt")

    wordList=set()
    bigrams=set()

    def __init__(self):
        self.loadWordList()
        self.loadBigrams()
        print("MyCorpus initiated :)\n")

    # def addCorpus(self, path):


    # def save(self):
    #     self.saveWordList()
    #     self.saveBigrams()

    # def saveWordList(self):
    #     try:
    #         wf=open(self.wordListPath, "w")
    #     except:
    #         raise IOError("Can't save wordlist in file.")
        

    def loadWordList(self):
        print("Fetching Wordlist...")
        try:
            wf=open(self.wordListPath, "r", encoding="utf-8")
        except:
            open(self.wordListPath, "w").close()
            wf=open(self.wordListPath, "r", encoding="utf-8")

        for word in wf:
            for w in word.split():
                self.wordList.add(w)
        wf.close()

        ### print all words
        print("Printing wordList: {}".format("<Empty>" if not self.wordList else ""))
        for i, word in enumerate(self.wordList):
            print(str(i+1), word)

        print("Loaded WordList\n")
    
    def loadBigrams(self):
        print("Fetching Bigrams...")
        try:
            bf=open(self.bigramPath, "r", encoding="utf-8")
        except:
            open(self.bigramPath, "w").close()
            bf=open(self.bigramPath, "r", encoding="utf-8")

        for line in bf:
            a, b = line.split()
            self.bigrams.add((a, b))
        bf.close()

        ### print all bigrams
        print("Printing bigrams: {}".format("<Empty>" if not self.bigrams else ""))
        for i, bigram in enumerate(self.bigrams):
            print(str(i+1), bigram[0], bigram[1])
        
        print("Loaded Bigrams\n")