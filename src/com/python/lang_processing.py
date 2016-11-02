'''
Created on Sep 23, 2016

@author: abhay.jain
'''
import nltk
from nltk.book import (text1,text3,FreqDist)
from nltk.util import bigrams
text1.concordance("monstrous") #Searching inside text
print("-----------------------------------------------")
print("Length of text1 : ",len(text1))
print(sorted(set(text3)))
print("Count of smote in text3 : ",text3.count("smote"))
print("Index of smote in text4 : ",text3.index('smote'))
fdist1 = FreqDist(text1)
print(fdist1)
#print(fdist1.items())
print(fdist1.most_common(50))
#print(text1.count("whale"))
print(fdist1["whale"])
print(fdist1.get("involuntarily"))

V = set(text1)
long_words = [w for w in V if len(w) > 12 and fdist1[w] > 10]
print(sorted(long_words))
for long_word in long_words:
    print(long_word + ": " +str(fdist1.get(long_word)))
    
print(list(bigrams(['more', 'is', 'said', 'than', 'done'])))
print(text1.collocations()) #A collocation is a sequence of words that occur together unusually often
fdist = FreqDist(len(w) for w in text1) #pair of length and count of words with that length
print(fdist)
print(fdist.items())
for item in fdist:
    print(item, fdist.get(item))

sent7=['Pierre', 'Vinken', ',', '61', 'years', 'old', ',', 'will', 'join', 'the',
'board', 'as', 'a', 'nonexecutive', 'director', 'Nov.', '29', '.']
print(fdist.tabulate())
print(sorted(w for w in set(text1) if '-' in w and 'index' in w))
print(sorted(wd for wd in set(text3) if wd.istitle() and len(wd) > 10))
print(sorted(w for w in set(sent7) if not w.islower()))
print(sorted(t for t in set(text1) if 'cie' in t or 'cei' in t))

from nltk.corpus import gutenberg,brown
print(nltk.FreqDist(gutenberg.words("C:\\Users\\abhay.jain\\Desktop\\text222.txt")).items())
print(nltk.corpus.gutenberg.fileids())
print(brown.categories())