'''
random functions and library
'''
import random

#the following function generates a random number between 1 and 6
temp = random.randint(1,6)
print(temp)

#the following function returns a random choice form list of elements
random.choice(['rock', 'paper', 'scissors'])

#display a string backwards
str1 = 'This is a sample sentence'
str1[::-1]

#Taking multiple input from the user
#use loops in this case
while True:
    str2 = input("Enter the input value: ")
    #checks if only enter was pressed
    if not str2:
        break