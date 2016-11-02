'''
Created on Sep 27, 2016

@author: abhay.jain
'''
import nltk
from nltk.corpus import gutenberg,brown,stopwords
from nltk.book import text1
from nltk.probability import FreqDist
print(nltk.FreqDist(gutenberg.words("C:\\Users\\abhay.jain\\Desktop\\text222.txt")).items())
print(gutenberg.fileids())
print(brown.categories())
print(brown.words(categories='news'))

t = [word for word in text1 if not word in stopwords.words("english")]
#print(FreqDist(t).items())
print(t.__len__())

t1 = [word for word in text1]
#print(FreqDist(t1).items())
print(t1.__len__())
#===============================================================================
# 
# t2 = [x for x in FreqDist(t1).items() if not x in FreqDist(t).items()]
# print(t2)
#===============================================================================

set1 = set(x for x in FreqDist(t).items())
set2 = set(x for x in FreqDist(t1).items())
print(len(set2.difference(set1)))