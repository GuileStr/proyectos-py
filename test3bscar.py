# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 10:36:23 2020

@author: palar
"""

arr = list(map(int, input('Array1: ').split()))
arr2 = list(map(int, input('Array2: ').split()))
con=0
for i in range(len(arr)):
    #print(arr[i])
    #print(arr2[i])
    if (arr[i]-arr2[i]) <=2 or (arr[i]-arr2[i])>=1 \
    or (arr[i]-arr2[i]) ==-2 or (arr[i]-arr2[i])==-1:
        con+=1
print(con)


 #if 1(arr[i]-arr2[i]) <=2