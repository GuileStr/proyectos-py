# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 14:12:24 2020

@author: palar
"""

def payment(b,ar,p,m):
    if m>11:
        return b
    else:
#        print("MONTH:",m)
#        print("b",m,"=",b)
        mpayment= round (b*p,2) #Balance * paymentrate
#        print("Minimum Payment=", b,"*",p,"==",mpayment)
        upb= round(b-mpayment,2) #Balance - mpayment = balance que falta por pagar
#        print("Unpaid balance=",b,"-",mpayment,"==",upb)
        i= round( (ar/12) * upb ,2) #Interes = payment rate / 12 * lo que falta de pagar
#        print("Interest=",ar,"/",p,"*",upb,"==",i)
        m+=1
        return round (payment(upb+i,ar,p,m),2)
        
        
#balance= 42
#annualInterestRate=0.2
#monthlyPaymentRate=0.04
months=0

print(payment(balance,annualInterestRate,monthlyPaymentRate,months))
