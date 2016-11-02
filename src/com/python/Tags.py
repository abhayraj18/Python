'''
Created on Sep 27, 2016

@author: abhay.jain
'''
import nltk
from nltk import word_tokenize
text = word_tokenize("And now for something completely different")
print(nltk.pos_tag(text))

text = word_tokenize("They refuse to permit us to obtain the refuse permit")
print(nltk.pos_tag(text))

text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
print(text.similar('woman')) #searching for woman finds nouns
print(text.similar('bought')) #searching for bought mostly finds verbs

from nltk.corpus import stopwords # Import the stop word list
print(stopwords.words("english"))

