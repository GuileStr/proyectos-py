# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:51:44 2020

@author: palar
"""

balance = 245059; annualInterestRate = 0.21
interes_mensual = annualInterestRate/12
lower = round(balance/12,2)
upper = round((balance*(1+interes_mensual)**12)/12,2)
valminimo = (lower+upper)/2
def calculo_interes_anual(balance,valminimo,interes_mensual):
    for i in range(12):
        balance = balance - valminimo
        balance = balance + (interes_mensual*balance)
    return balance
while True:
    ans=calculo_interes_anual(balance,valminimo,interes_mensual)
    if ans <=0.01 and ans >= 0.001:
        print("Lowest Payment: " + str(round(valminimo,2)))
        break
    elif ans > 0.01:
        lower = valminimo
    elif ans < 0.0009:
        upper = valminimo
    valminimo = (lower+upper)/2