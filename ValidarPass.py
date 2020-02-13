# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:40:10 2020

@author: palar
"""
def vali(password):
    mayus=0
    minus=0
    digit=0
    noalfa=0
    if password.isalnum!=True:
        for i in password:
            if i.isupper()==True: #Si es mayus
                mayus=1
            elif i.islower()==True: #Si es minuscula
                minus=1
            elif i.isdigit()==True: #Si es un numero
                digit=1
            elif i.isalnum()!=True: #Si es diferente alfanumerico
                noalfa=1
            elif i == "":
                break
            else:
                break
    else:
        print('La contraseña elegida no es segura')    
    if mayus>0 and minus>0 and digit>0 and noalfa>0:
        print('Jala')
        return True
    else:
        print('La contraseña elegida no es segura')
        return False

password = input()
tes = vali(password)