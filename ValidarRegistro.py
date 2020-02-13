# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:41:09 2020

@author: palar
"""
import getpass

def validarUser(name):
    if len(name)<6:
        print('El nombre de usuario debe contener al menos 6 caracteres')
    elif len(name)>12:
        print('El nombre de usuario no puede contener más de 12 caracteres')
    elif name.isalnum()!=True:
        print('El nombre de usuario puede contener solo letras y números')
    else:
        return True
def validarPas(pwd):
    mayus=0
    minus=0
    digit=0
    noalfa=0
    if pwd.isalnum!=True:
        for i in pwd:
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
    

print("Que tal, amiko")
user = input('Ingresa el usuario: ')
pas = getpass.getpass('Ingresa pass: ');# esto debería convertirlo en **
#No se hace asteriscos por la version pyton/spiders
uval = validarUser(user)
pval = validarPas(pas)
if uval==True and pval==True:
    print('Puede registrarse sin problemas')
elif uval==True and pval==False:
    print("Parece que algo salió mal con la password")
elif uval==False and pval==True:
    print("Parece que algo salió mal en el usuario")
else:
    print("Parece que ambos campos son incorrectos.. por favor verificalos y los mensajes anteriores para poder registrar exitosamente")