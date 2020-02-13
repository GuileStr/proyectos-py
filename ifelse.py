# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 13:56:53 2020

@author: palar
"""

x = int(input('jeje: '))
if x%4==0:
    if x%100==0:
        print("False")
    elif x%400==0:
        print("True")
else:
    print("False")