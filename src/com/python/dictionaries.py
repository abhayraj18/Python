'''
Created on Sep 23, 2016

@author: abhay.jain
'''
from collections import defaultdict
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781

print(phonebook)
for name, number in phonebook.items():
    print ("Phone number of "+name+" is "+ str(number))
    
if "Jill" in phonebook:
    print ("Jill is listed in the phonebook.")
if "Jake" not in phonebook:
    print ("Jake is not listed in the phonebook.")

del phonebook["John"] #phonebook.pop("John")
print(phonebook)
#===============================================================================
# can also declare like this
#  phonebook = {
#      "John" : 938477566,
#      "Jack" : 938377264,
#      "Jill" : 947662781
#  }
#===============================================================================

#default dictionaries, creates an entry with default value if key does not exist
frequency = defaultdict(int)
frequency['colorless'] = 4
frequency['ideas']
print(frequency)

pos = defaultdict(list)
pos['sleep'] = ['NOUN', 'VERB']
pos['ideas']
print(pos)

pos = defaultdict(lambda: 'NOUN') #default value
print(pos['abhay'])

pos.update({'cats': 'N', 'scratch': 'V', 'peacefully': 'ADV', 'old': 'ADJ'})
print(pos)



#===============================================================================
# Example    Description
# d = {}    create an empty dictionary and assign it to d
# d[key] = value    assign a value to a given dictionary key
# d.keys()    the list of keys of the dictionary
# list(d)    the list of keys of the dictionary
# sorted(d)    the keys of the dictionary, sorted
# key in d    test whether a particular key is in the dictionary
# for key in d    iterate over the keys of the dictionary
# d.values()    the list of values in the dictionary
# dict([(k1,v1), (k2,v2), ...])    create a dictionary from a list of key-value pairs
# d1.update(d2)    add all items from d2 to d1
# defaultdict(int)    a dictionary whose default value is zero
#===============================================================================