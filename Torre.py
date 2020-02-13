# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 12:17:12 2020

@author: palar
"""

def printMoves(fr,to):
    print("Move from",fr,"to",to)
def Towers(n,fr,to,spare):
    if n==1:
        printMoves(fr,to)
    else:
        Towers(n-1,fr,spare,to)
        Towers(1,fr,to,spare)
        Towers(n-1,spare,to,fr)
        
print(Towers(4,'Grande','mediano','chico'))