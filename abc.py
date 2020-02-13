# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 16:38:50 2020

@author: palar
"""

s = 'abcbcd'
ans=''  #Aqui guardo la respuesta o posible respuesta
t=''    #Aqui guardo temporalmente la posible respuesta
for i in range(len(s)): #Ciclo numerico del tamaño del string
    t+=s[i] #Guardo de forma temporal la letra en S en la posicion i
    if len(t)>len(ans): # Si t es más grande que ans los igualamos
        ans=t   #Empatamos ans y t
    if i > len(s)-2: #Si i es mayor a la posicion de s-2 se sale del ciclo
        break
    if s[i]>s[i+1]: #Si la letra de s en la posicion i es mas grande a la de s en la i+1
        t=''        #Lo borramos (No mas grande numericamente... si no en el abcd "Ej: A<B. A=1 y B=2")

print('Longest substring in alphabetical order is: '+ans)