# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:55:44 2020

@author: palar
"""

x=25
epsilon=0.0001
numGuesses= 0
low=1.0
high=x
ans=(high+low)/2.0

while abs(ans**2-x)>=epsilon:
    print(abs(ans**2))
    print(abs(ans**2-x))
    print(ans)
    print("Low =",str(low),"High =",str(high),"answer =",str(ans))
    numGuesses+=1
    if ans**2<x:
        low=ans
    else:
        high=ans
    ans = (high+low)//2.0
#    nump= ((high+low)//2.0)+1
print("Num de guesses:",numGuesses)
print(str(ans)+", es lo mas cerca a raiz de:", str(x))



##
#x = 25
#epsilon = 0.01
#step = 0.1
#guess = 0.0
#
#while abs(guess**2-x) >= epsilon:
#    if guess <= x:
  #      guess += step
 #   else:
#        break

#if abs(guess**2 - x) >= epsilon:
#    print('failed')
#else:
#    print('succeeded: ' + str(guess))