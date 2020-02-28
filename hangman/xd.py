# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 12:30:37 2020

@author: palar
"""
def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here
    for i in range(len(L)-1):
        #print(L[i])
        if L[i]!='a':
            L.remove(L[i])
    return len(L)

#run_satisfiesF(L, satisfiesF)

def f(s):
    return 'a' in s
      
L = ['a', 'b', 'a']

#print(f(L))
print(satisfiesF(L))

print(L)
