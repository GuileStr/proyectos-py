# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:45:03 2020

@author: palar
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr=='':
        return False
    size=(len(aStr)//2)
    #print("Arreglo "+aStr)
    #print("Longitud del arreglo",len(aStr))
    #print("mitad del arreglo",size+1)
    if char==aStr[size]:
        return True
    
    elif size<1 and char!=aStr[size]:
        return False
    elif char<aStr[size]:
        #print("Esta en izq, en esto "+aStr[:size])
        aStr=aStr[:size]
        return isIn(char,aStr)
    elif char>aStr[size]:
        #print("Esta en derecha, en esto "+aStr[size:])
        aStr=aStr[size:]
        return isIn(char, aStr)
    
    
print(isIn('i',''))