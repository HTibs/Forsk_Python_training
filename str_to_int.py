'''
# Clean the Messy salary into integers for Data Processing
salary = '$876,001' 

Hint:
    Remove the $
    Remove the ,
    Convert into integer
'''

#Clean the messy salary into integers for Data Processing 

str ='$876,001'
temp =''

for x in str:
    if x.isdigit():
        temp+=x

value =int(temp)
print(type(value))
print(value)