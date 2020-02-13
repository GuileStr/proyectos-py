# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 09:30:45 2020

@author: palar
"""

#def is_even(i):
#    """
#        input: i, positive int
#    """
#    return(i%2==0)
    
#print(is_even(3))
#def sq(i):
#    """
#        square
#    """
#    return(x**2)
#x=3
#print(sq(x))
def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return( (a * x**2)+(b * x)+c)

print(evalQuadratic(1,2,3,4))