
"""
Name: 
    Clean the Messy salary from list        
Filename:
    salary2.py
Problem Statement:
    salaries = ['$876,001', '$543,903', '$2453,896'] 
    Clean the Messy salaries into integers for Data Processing
    Remove the $
    Remove the ,
    Convert into integer
Hint: 
    We can use slicing concept to remove $ or remove() method 
    We can use the split and join to remove the , comma
    We canuse the int() typecast to convert into integer
"""

salaries = ['$876,001', '$543,903', '$2453,896']
temporary = []
for index, x in enumerate(salaries, start=0):
    temp=''
    for y in x:
        if y.isdigit():
            temp+=y
    value =int(temp)
    temporary.append(value)
    index+=1
salaries=temporary.copy()
print(salaries)