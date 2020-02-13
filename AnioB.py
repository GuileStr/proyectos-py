# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:34:06 2020

@author: palar
"""

def is_leap(year):
    leap = False
    if year%4==0 and year%100==0 and year%400==0:
        leap=True
    else:
        leap=False    
    # Write your logic here
    
    return leap

year = int(input())
l = is_leap(year)
print(l)