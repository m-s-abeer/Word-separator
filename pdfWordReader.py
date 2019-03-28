# importing required modules 
import PyPDF2
import nltk
from my_corpus import MyCorpus as mc
lib=mc()
import re

def isWord(word):
        if(len(word)<3): return False
        for char in word:
                if not char.isalpha(): return False
        return True

def main():
    origFileName = 'my_corpus\cambridge_dic.pdf'
    # creating a pdf file object 
    wf=open('my_corpus\cambridge_words2.txt', "w", encoding="utf-8")
    
    # creating a pdf reader object 
    pdfReader = PyPDF2.PdfFileReader(origFileName) 
    
    # printing number of pages in pdf file
    regexp = r'\b\w+\b'
    pages=int(pdfReader.numPages)
    words=list()
    for pageid in range(pages):
#     for pageid in range(1):
        pageObj = pdfReader.getPage(pageid)
        data=pageObj.extractText()
        all_words=re.findall(regexp, str(data))
        # print(all_words)
        # print([word.lower() for word in all_words if isWord(word)])
        words.extend([word.lower() for word in all_words if isWord(word)])
    
    # extracting text from page 
    
    set_words=set()
    for word in words:
            set_words.add(word)

    print(len(set_words))
    for word in set_words:
            wf.write(word+'\n')

    
    # closing the pdf file object 
    wf.close()
      
if __name__ == "__main__": 
    # calling the main function 
    main() 