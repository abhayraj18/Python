'''
Created on Sep 24, 2016

@author: abhay.jain
'''
def fib():
    a, b = 1, 1
    while 1:
        print("hiiiii")
        yield a
        print("hi")
        a, b = b, a + b

# testing code
import types
if type(fib()) == types.GeneratorType:
    print ("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print (n)
        print("hellloooo")
        counter += 1
        if counter == 10:
            break