'''
Created on Sep 26, 2016

@author: abhay.jain
'''
from functools import partial
def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x

p = partial(func,5,6,7) #5 -> u, 6 -> v, 7 -> w
print(p(8)) #8 -> x
