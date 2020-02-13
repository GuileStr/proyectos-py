# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 16:22:13 2020

@author: palar
"""

num=12
neg=False
if num<0:
    neg=True
    num=abs(num)
else:
    neg=False
result=''
if num == 0:
    result='0'
while num>0:
    result= str(num%2)+result
    num=num//2
if neg:
    result = '-'+result
    
print(result)