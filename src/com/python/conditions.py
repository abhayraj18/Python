'''
Created on Sep 23, 2016

@author: abhay.jain
'''
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")
elif name == "John" or name == "Rick":
    print("Your name is either John or Rick.")
else:
    print("Abhay")

nameList = ["John", "Rick"]
if name in nameList:
    print("Your name is either John or Rick.")