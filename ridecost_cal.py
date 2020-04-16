# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 18:58:04 2020

@author: HT
"""
# Ride Cost Calculator

'''
    travel 80km to and fro
    diesel- rs80/lt
    fuel avg 18km/lt
    ??cost of driving per day to office
'''

dist_travelled = int(input("Enter the distance travelled: "))
diesel_cost = int(input("Enter the cost of diesel per litre: "))
fuel_average = float(input("Enter the fule average of the car"))

fuel_consumed = dist_travelled/fuel_average
travel_cost= fuel_consumed*diesel_cost

print("The cost of your travel is: %f" %(travel_cost))
    