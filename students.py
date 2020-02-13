# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:34:54 2020

@author: palar
"""

ns= int(input("numero de estudiantes: "))
st={}
x=0
while x!=ns:
    name= input("nombre: ")
    cal= int(input("cal: "))
    st[name]=cal
    x+=1

calx = st.values()
print(st)
print(calx)
