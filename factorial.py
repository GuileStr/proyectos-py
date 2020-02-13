# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 11:24:41 2020

@author: palar
"""
##RECURSION
def fact(n):
    if n==1:
        return 1
    else:
#        print(n*fact(n-1))
        return n*fact(n-1)

print(fact(3))

##Iteracion
def factit(n):
    prod=1
    for i in range(1,n+1):
        prod*=i
    return prod

print(factit(4))
        