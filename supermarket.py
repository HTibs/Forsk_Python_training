
"""
Name: 
    Supermarket      
Filename:
    supermarket.py 
Problem Statement:
    You are the manager of a supermarket. 
    You have a list of items together with their prices that consumers bought on a particular day. 
    Your task is to print each item_name and net_price in order of its first occurrence. 
    Take Input from User   
Hint: 
    item_name = Name of the item. 
    net_price = Quantity of the item sold multiplied by the price of each item.
    try to use new class for dictionary : OrderedDict 
Sample Input:
    BANANA FRIES 12
    POTATO CHIPS 30
    APPLE JUICE 10
    CANDY 5
    APPLE JUICE 10
    CANDY 5
    CANDY 5
    CANDY 5
    POTATO CHIPS 30
Sample Output:
    BANANA FRIES 12
    POTATO CHIPS 60
    APPLE JUICE 20
    CANDY 20
""" 

itemlist=dict()
while True:
    item=input("Enter the item and quantity split by ,\n")
    if(item!=''):
        key, value = item.split(",")
        if key in itemlist.keys():
            newval = int(value)+int(itemlist[key])
            itemlist[key]=str(newval)
            continue
        itemlist[key]=value
    else:
        break
#print(itemlist)
print("Output")
for key, val in itemlist.items():
    print(key, ' : ', value)

