# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:58:54 2020

@author: palar
"""

def bisec(l,h):
    print("low= "+str(l)+" y high= "+str(h))        
    return (high+low)//2

low=0.0
high=100
ans=(high+low)/2.0
tru=True


print("Please think of a number between 0 and 100!")
while tru==True:
    print("Is yout secret number "+str(ans)+"?")
    dec=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if dec=='l':
        low=ans
        print("Muy bajo. Ahora low=",ans)
        ans=bisec(low,high)
    elif dec=='h':
        high=ans
        print("Muy alto. Ahora high=",ans)
        ans=bisec(low,high)
    elif dec=='c':
        tru=False
    else:
        print("Sorry, I did not understand your input.")
print("Game over. Your secret number was:",ans)    

#Este es el print que va dentro del ciclo
#value= input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")