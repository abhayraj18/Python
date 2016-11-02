'''
Created on Sep 26, 2016

@author: abhay.jain
'''
def do_stuff_with_number(n):
    print(n)

the_list = (1, 2, 3, 4, 5)

for i in range(20):
    try:
        do_stuff_with_number(the_list[i])
    except IndexError: # Raised when accessing a non-existing index of a list
        do_stuff_with_number(0)
        
actor = {"name": "John Cleese", "rank": "awesome"}

#Function to modify, should return the last name of the actor - think back to previous lessons for how to get it
def get_last_name():
    try:
        return actor["last_name"]
    except KeyError:
        return "Cleese"

def getRank():
    return actor["rank"]

print("All exceptions caught! Good job!")
print("The actor's last name is ", get_last_name() +", Rank : ", getRank())