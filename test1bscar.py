# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 09:23:28 2020

@author: palar
"""
n=int(input('Ingresa la longitud del array: '))
arr = list(map(int, input().split()))
#arr = list(map(int, input().split()[:n]))
if n==0 and len(arr)==0:
    print('Lista muy corta para comparar tamaños.')
elif n==1 and len(arr)==1:
    print('Así que el más grande es: ',arr,", y pues su diferencia con el menor es el mismo")
elif len(arr)>n:
    print('Tu array es más grande de lo que dijiste.. pero ahí te baila.')
    m=max(arr)
    men=min(arr)
    dif=m-men
elif n>len(arr):
    print('La longitud es más grande quel array que pusiste')
else:
    m=max(arr)
    men=min(arr)
    dif=m-men
print('diferencia es: ',dif)