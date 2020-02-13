# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 09:37:05 2020

@author: palar
"""
def evaluar():
    if cu==1:
        print(1)
    if cd==2:
        print(2)
    if ct==3:
        print(3)
    if cc==4:
        print(4)

arr = list(map(int, input('Pasa el array plocs: ').split()))
cu=0
cd=0
ct=0
cc=0
if len(arr)>1:
    for i in range(len(arr)):
    #print(arr[i])
        if arr[i]==1:
            cu+=1
        elif arr[i]==2:
            cd+=1
        elif arr[i]==3:
            ct+=1
        elif arr[i]==4:
            cc+=1
        evaluar()
elif min(arr)<0:
    print('No puedes meter negativos compa')
elif len(arr)==1:
    for i in range(len(arr)):
    #print(arr[i])
        if arr[i]==1:
            cu+=1
        elif arr[i]==2:
            cd+=1
        elif arr[i]==3:
            ct+=1
        elif arr[i]==4:
            cc+=1
        evaluar()