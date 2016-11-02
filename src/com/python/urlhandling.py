'''
Created on Sep 26, 2016

@author: abhay.jain
'''
import nltk
from nltk import word_tokenize
from urllib import request
url = "http://www.gutenberg.org/files/2554/2554.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
print(type(raw))
print(len(raw))
print(raw[:100])
tokens = word_tokenize(raw)
print(type(tokens))
print(tokens[:10])

text = nltk.Text(tokens)
print(text.collocations())