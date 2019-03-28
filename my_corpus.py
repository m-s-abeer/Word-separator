import os

class MyCorpus:
    cambridgePath=os.path.abspath("my_corpus/cambridge_words.txt")
    wordListPath=os.path.abspath("my_corpus/wordList.txt")
    bigramPath=os.path.abspath("my_corpus/bigrams.txt")

    wordList=set()
    bigrams=set()
    debug=False

    def __init__(self, debug=False):
        self.loadWordList()
        self.loadBigrams()
        self.loadCambridgeWords()
        self.debug=debug
        print("MyCorpus initiated :)\n")

    def saveAll(self):
        self.saveWordList()
        self.saveBigrams()

    def addWord(self, word):
        self.wordList.add(word)

    def addBigram(self, word):
        self.bigrams.add(word)

    def saveWordList(self):
        try:
            wf=open(self.wordListPath, "w", encoding="utf-8")
        except:
            raise IOError("Can't save wordlist in file.")
        for word in self.wordList:
            wf.write(word+"\n")
        wf.close()

    def saveBigrams(self):
        try:
            wf=open(self.bigramPath, "w", encoding="utf-8")
        except:
            raise IOError("Can't save wordlist in file.")
        for line in self.bigrams:
            wf.write(line[0]+" "+line[1]+"\n")
        wf.close()
    
    def printAllWords(self):
        print("Printing wordList: {}".format("<Empty>" if not self.wordList else ""))
        for i, word in enumerate(self.wordList):
            print(str(i+1), word)

    def printAllBigrams(self):
        print("Printing bigrams: {}".format("<Empty>" if not self.bigrams else ""))
        for i, bigram in enumerate(self.bigrams):
            print(str(i+1), bigram[0], bigram[1])

    def loadCambridgeWords(self):
        print("Fetching Cambridge Words...")
        try:
            wf=open(self.cambridgePath, "r", encoding="utf-8")
        except:
            open(self.wordListPath, "w").close()
            wf=open(self.cambridgePath, "r", encoding="utf-8")

        for word in wf:
            for w in word.split():
                self.wordList.add(w)
        wf.close()

        if self.debug: self.printAllWords()
        print("Loaded Cambridge Words\n")

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

        if self.debug: self.printAllWords()
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

        if self.debug: self.printAllBigrams()
        print("Loaded Bigrams\n")