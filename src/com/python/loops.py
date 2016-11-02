'''
Created on Sep 23, 2016

@author: abhay.jain
'''
# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print (x)

print("--------------------------")
# Prints out 3,4,5
for x in range(3, 6):
    print (x)

print("--------------------------")
# Prints out 3,5,7 i.e numbers b/w 3 and 8 starting with 3 with gap of 2
for x in range(3, 8, 2):
    print (x)
    
print("--------------------------")
primes = [2, 3, 5, 7]
for prime in primes:
    print (prime)
    
print("While--------------------------")
count = 0
while count < 5:
    print (count)
    count += 1  # This is the same as count = count + 1
    
