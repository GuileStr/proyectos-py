# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 14:12:24 2020

@author: palar
"""

def payment(b,ar,c,m):
    if m>11:
        return b
    else:
        #print("MONTH:",m)
        #print("Pagos de=",c)
       # print("b",m,"=",b)
        mir= ar/12
        #print("Monthly annual rate=",mir)
        mupb=b - c
        #print("Monthly unpaid balance",mupb)
        ubem=mupb+ (mir*mupb)
        #print("Updated balance each month",ubem)
        #i= round( (ar/12) * mupb ,2)
        #print("Interes=",i)
        m+=1
        return payment(ubem,ar,c,m)
        
#balance= 3329
#annualInterestRate=0.2
c=10
months=0
x=False
while x==False:
    a = payment(balance,annualInterestRate,c,months)
    if a<0:
        print("Lowest Payment:",c)
        break
    else:
        c+=10
#print(a)