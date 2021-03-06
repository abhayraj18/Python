'''
Created on Sep 23, 2016

@author: abhay.jain
'''
data = ("John", "Doe", 53.44)
format_string = "Hello"

print("%s" %format_string + " %s %s. Your balance is %.2f $." %(data[0], data[1], data[2]))

astring = "Hello world!"
print(astring[3:9])
print(astring[3:9:2]) #characters from index 3 to 9 with 2 gaps
print(astring[::-1]) #Reversing
print(astring[-2]) #-ve index starts from back
print("Index of world : ",astring.find("world"))

a = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]
b = [' ' * 2 * (7 - i) + 'very' * i for i in a]
for line in b:
    print(line)
    
phrase = 'And now for something completely different'
if 'thing' in phrase:
    print('found "thing"')
    
#===============================================================================
# Method    Functionality
# s.find(t)    index of first instance of string t inside s (-1 if not found)
# s.rfind(t)    index of last instance of string t inside s (-1 if not found)
# s.index(t)    like s.find(t) except it raises ValueError if not found
# s.rindex(t)    like s.rfind(t) except it raises ValueError if not found
# s.join(text)    combine the words of the text into a string using s as the glue
# s.split(t)    split s into a list wherever a t is found (whitespace by default)
# s.splitlines()    split s into a list of strings, one per line
# s.lower()    a lowercased version of the string s
# s.upper()    an uppercased version of the string s
# s.title()    a titlecased version of the string s
# s.strip()    a copy of s without leading or trailing whitespace
# s.replace(t, u)    replace instances of t with u inside s
#===============================================================================