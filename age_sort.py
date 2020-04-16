"""
Take the age as input from the user and print whether he is a infant, Child , 
Adult,  Senior Citizen
0 - 1 is Infant
> 1 and < than 18 is Child 
> 18 and < 60 is Adult
> 60 is Senior Citizen 
"""

#Age Category calculate

age = int(input("Enter age of the person: "))
#int(age)
if (age==0 or age ==1):
    print("INFANT")
elif (age>=2 and age<19):
    print("CHILD")
elif (age>=19 and age<60):
    print("ADULT")
else:
    print("SENIOR CITIZEN")