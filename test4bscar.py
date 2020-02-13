# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 11:08:26 2020

@author: palar
"""

def multiplo(value,mul):
    if value%mul==0:
        return True
    else:
        return False

start = int(input('Start: '))
end = int(input('End: '))
arr=[]
for i in range(start,end):
    t3 = multiplo(i,3)
    t5 = multiplo(i,5)
    
    if t3==True:
        #print(i," multiplo de 3")
        arr.append("Fizz")
    
    elif t5==True:
        arr.append("Buzz")
        #print(i," multiplo de 5")
    elif t3==True and t5 == True:
        arr.append("FizzBuzz")
        #print("Multiplo de ambos")
    elif t3!=True or t5!=True:
        arr.append(i)
        #print("Multiplo de nada unu")
        
print(arr)