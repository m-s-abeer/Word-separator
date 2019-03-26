import nltk
from nltk.corpus import wordnet as wn
synonyms=[]
cnt=int(0)
for word in wn.words():
    print(word)
    cnt+=1
    if(cnt==1000):
        break
print(cnt)
print("doing" in wn.words())

# from word_forms.word_forms import get_word_forms
# # help(get_word_forms)
# get_word_forms("elect")