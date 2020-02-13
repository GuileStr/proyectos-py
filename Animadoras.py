# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:08:28 2020

@author: palar
"""

an_letters="aefhilnorsxAEFHILNORSX"

word = input("Te aiuro a echar porras: ")
times = int(input("¿Cuantas veces lo quieres gritar? "))
var=0
while var<len(word):
    char= word[var]
    if char in an_letters:
        print("Give me an: ",char,"!!")
    else:
        print("Give me a: "+char+"!!")
    var+=1
print("¿Y que dice? uwu")
for i in range(times):
    print(word+"!!!")