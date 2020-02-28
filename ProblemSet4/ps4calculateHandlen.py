# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 14:55:15 2020

@author: palar
"""

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    return sum(hand.values())
    

print(calculateHandlen({'a': 3, 'u': 1, 'e': 1, 'r': 1, 't': 1, 'p': 2}))