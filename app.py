# import library_generator as lg
from my_corpus import MyCorpus as mc


### Gets query text and returns word tokens
def query(qText=""):
    print(qText)
    ### Run aho-corasick and generate lists of possible words in each end-points
    ### Call brute-force for smaller sentences
    ### Try randomized algorithm for larger sentences


### Program starts from here
# updateCorpus()

# get Corpus
lib = mc()


# take queries
# while(True):
#     qText=input("Enter your query sentence: ")
#     print('Your query: "' + qText + '"')
#     # print(query(qText))