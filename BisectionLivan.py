# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:51:44 2020

@author: palar
"""

balance = 245059; annualInterestRate = 0.21
interes_mensual = annualInterestRate/12
#print("interes mensual: ",interes_mensual)
lower = round(balance/12,2)
#print("lower: ",lower)
upper = round((balance*(1+interes_mensual)**12)/12,2)
#print("upper: ",upper)
cuota_minima = (lower+upper)/2
def calculo_interes_anual(balance,cuota_minima,interes_mensual):
    for i in range(12):
        balance = balance - cuota_minima
        #print("balance pagando la cuota minima de: ",cuota_minima," quedando: ",balance)
        balance = balance + (interes_mensual*balance)
        #print("balance mas interes: ",balance)
    return balance
#print(calculo_interes_anual(balance,29157.09,interes_mensual))
while True:
    awa=calculo_interes_anual(balance,cuota_minima,interes_mensual)
    #print(awa)
    if awa <=0.01 and awa >= 0.001:
        print("Lowest Payment: " + str(round(cuota_minima,2)))
        break
    elif awa > 0.01:
        #print(cuota_minima)
        lower = cuota_minima
        #print("cuota muy baja")
    elif awa < 0.0009:
        #print(cuota_minima)
        upper = cuota_minima
        #print("cuota muy alta")
    cuota_minima = (lower+upper)/2