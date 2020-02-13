# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:35:58 2020

@author: palar
"""

cube=27
epsilon=0.01
guess=0.0
increment=0.0001
num_guesses=0
while abs(guess**3-cube)>=epsilon:
    guess+=increment
    num_guesses+=1
print("Tanteado:",num_guesses)
if abs(guess**3-cube)>=epsilon:
    print("Te fallé Albert")
else:
    print(guess,"cerca de la raiz de:",cube)