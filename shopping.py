'''
Name: 
    Shopping List        

'''

print("This is an application to create a shopping list")
print('Enter all the items one by one.')
print("At the end of your items list enter DONE (all caps)")

items=[]
index=0
temp=''
while True:
    temp = input('Enter an item or DONE to exit: ')
    if(temp=='DONE'):
        break
    else:
        items.insert(index,temp)
        index=index+1
print(items)
    