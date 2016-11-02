'''
Created on Sep 26, 2016

@author: abhay.jain
'''
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])
print(len(b))
print(a.intersection(b))
print(a.symmetric_difference(b))
print(a.difference(b))
print(b.difference(a))
print(a.union(b))