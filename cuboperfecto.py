# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:42:54 2020

@author: palar
"""

x = int(input('Ingresa un entero: '))
ans=0
while ans**3 < x:
    ans+=1
if ans**3 !=x:
    print(str(x)+", no es perfecto")
else:
    print("Cube root of "+str(x)+" is "+str(ans))
    
#La forma mas limpia es:
    
for guess in range(x+1):
    if guess**3 == x:
        print("Raiz cuadrada de:", x, " es: ",guess)
    else:
        print("No tiene raiz")
