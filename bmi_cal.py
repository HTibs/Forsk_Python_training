# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 18:58:04 2020

@author: HT
"""
# Adult Body Mass Index Calculator

height= int(input("Enter your height in mtr"))
weight= int(input("Enter your weight in kgs"))
temp = weight/height
ans = temp/height

print("Your BMI is: %f" %(ans))