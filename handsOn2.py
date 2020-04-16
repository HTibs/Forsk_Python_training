'''
                                            list
'''

list1 = [1,2,3,4]
#this is called                             deep copy
list2=list1
print(list1)
print(list2)

# to add a new item in a list
list2.append(5)

print(list1)
'''
in the above print statement list1 also has got a new item although we only added the 
5 to list2. this happens because list1 and list2 share the same memory address
this is deep copy
'''
# to check the address of a variable we use id
id(list1)
id(list2)

#                                    shallow copy
#copy two lists without same address

list1 = [1,2,3,4]

list2 = list1.copy()

list2.append(5)

print(list1)
print(list2)
'''
in this case a new list with an other address and memory space is created 
thus changes in list2 are not reflected in list1
'''

# for loops and lists
list1[1,2,3,4]
for item in list1:
    print(list1)
    
                               #enumerate in list

for item in enumerate(list1):
    print(item)
    
"""
enumerate returns a tuple of index and list item
this is due to packing and unpacking of item in the list
"""

#                                    range and lists

#returns a list from 0 to the given range 5 is not included
list1 = list(range(5))
#returns a list from specified index to the other specified index
list2 = list(range(-1, 10))
#returns from strt index to the end index with stepper
list3 = list(range(1,50,2))

print(list1, list2, list3)

'''
                                    coding pattern problem
'''

'''
*
**
***
****
*****
****
***
**
*
'''
for item in range(1,6):
    print(item*"*")
for item in range(4,0,-1):
    print(item*"*")


'''
remove vowels from a list of word
input = ['alabama', 'cslifornia']
output = ['lbm','cslfrn']
'''

list1 = ['Alabama', 'California', 'Oklahama', 'Florida']
list2=[]
for value in list1:
    newvalue = ''
    for subvalue in value:
        if (subvalue not in 'aeiouAEIOU'):
            print(subvalue)
            newvalue = newvalue+subvalue
    list2.append(newvalue)        
print(list2)





'''
return sum of number in an array or list
return 0 if array empty
except number 13 and the number that will come immediately after 13
input = [13,1,2,13,2,1,13]
output = 3
'''

list1 = [13,1,2,13,2,1,13]
sum1 =0
index = 0
while(index < len(list1)):
#for item in list1:
    if(list1[index] == 13):
        index = index +2
        continue
    else:
        sum1 = sum1+list1[index]
        index = index+1
print(sum1)