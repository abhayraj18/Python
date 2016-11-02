'''
Created on Sep 23, 2016

@author: abhay.jain
'''
sent = ['word1', 'word2', 'word3', 'word4', 'word5','word6', 'word7', 'word8', 'word9', 'word10']
for x in sent:
    print(x)

print("All words with size > 4 : ",all(len(w) > 4 for w in sent))
print("Any word with size > 4 : ",any(len(w) > 4 for w in sent))
print(sent)
print(sent[5:]) # sublist from 5th index to last
print(sent[:5]) # sublist from start to 5th index
sent[0] = 'abhay'
print(sent)
print("length : ", len(sent))
tokens = sorted(sent)
print(tokens)
print(sent[-2:]) #sublist from second last to end
del sent[-1] #delete last item
print("After deleting : ",sent)

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
    if word != "the":
        word_lengths.append(len(word))
print(word_lengths)

#list comprehension of above example
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
print(words)
word_lengths = [len(word) for word in words if word != "the"]
print(word_lengths)

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(x) for x in numbers if x > 0]
print(newlist)

words = ['I', 'turned', 'off', 'the', 'spectroroute']
tags = ['noun', 'verb', 'prep', 'det', 'noun']
print(list(zip(words, tags)))
print(list(enumerate(words)))
