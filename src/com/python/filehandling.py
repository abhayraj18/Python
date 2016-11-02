'''
Created on Sep 26, 2016

@author: abhay.jain
'''
f = open("C:\\Users\\abhay.jain\\Desktop\\text222.txt")
#print(f.read())
for line in f:
    print(line.strip())
f.close()

f1 = open("C:\\Users\\abhay.jain\\Desktop\\abc.txt", "w")
f1.write("hello")
f1.close()