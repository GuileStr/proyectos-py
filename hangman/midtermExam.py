# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 09:01:23 2020

@author: palar
"""
# =============================================================================
# def laceStringsRecur(s1, s2):
#     """
#     s1 and s2 are strings.
# 
#     Returns a new str with elements of s1 and s2 interlaced,
#     beginning with s1. If strings are not of same length, 
#     then the extra elements should appear at the end.
#     """
#     def helpLaceStrings(s1, s2, out):
#         if s1 == '':
#             #PLACE A LINE OF CODE HERE
#         if s2 == '':
#             #PLACE A LINE OF CODE HERE
#         else:
#             #PLACE A LINE OF CODE HERE
#     return helpLaceStrings(s1, s2, '')
# 
# 
# 
# =============================================================================

def dict_invert(d):
    new={}
    dV=list(d.values())
    dK=list(d.keys())
    l=[]
    for i in range(len(d)):
        l.append(dK[i])
        print(dV[i]," = ",l)
        new[dV[i]]=l[i:]
    return new
d = {1: 1, 2: 1}
#print(dict_invert(d))

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    L[:]=L[::-1]
    for i in range(len(L)):
        tmp=L[i]
        L[i]=tmp[::-1]
L = [[0, 1, 2], [1, 2, 3]]
deep_reverse(L)
print(L)

# =============================================================================
#     print("L invertida",L)
#     for i in range(len(L)):
#         temp=L[i]
#         L[i]=temp[::-1]
#         #print("Despues",temp[::-1])
#         #Ltemp.append(temp)
#         #print("nueva ",Ltemp)
#         #print()i[::-1]
# =============================================================================
    

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ======================================HORRIBLE=======================================
# def jumpAndBackpedal(guess):
#     '''
#     isMyNumber: Procedure that hides a secret number. 
#      It takes as a parameter one number and returns:
#      *  -1 if the number is less than the secret number
#      *  0 if the number is equal to the secret number
#      *  1 if the number is greater than the secret number
#  
#     returns: integer, the secret number
#     ''' 
# #    guess = 1
#     if isMyNumber(guess) == 1:
#         return guess
#     foundNumber = False
#     while not foundNumber:
#         sign = isMyNumber(guess)
#         if sign == -1:
#             guess *= 2
#         else:
#             guess -= 1
#     return guess
# ========================================HORRIBLE=====================================
# =============================================================================
# def jumpAndBackpedal(isMyNumber):
#     '''
#     isMyNumber: Procedure that hides a secret number. 
#      It takes as a parameter one number and returns:
#      *  -1 if the number is less than the secret number
#      *  0 if the number is equal to the secret number
#      *  1 if the number is greater than the secret number
#  
#     returns: integer, the secret number
#     ''' 
#     guess = 1
#     if isMyNumber(guess) == 1:
#         return guess
#     foundNumber = False
#     while not foundNumber:
#         sign = isMyNumber(guess)
#         if sign == -1:
#             guess *= 2
#         else:
#             guess -= 1
#     return guess
# =============================================================================
# ===================================RINGUIN==========================================
#
#def isMyNumber(x):
#    mN=78
#    if x==mN:
#        return 0
#    elif x<mN:
#        return -1
#    elif x>mN:
#        return 1
#def jumpAndBackpedal(guess):
#     '''
#     isMyNumber: Procedure that hides a secret number. 
#      It takes as a parameter one number and returns:
#      *  -1 if the number is less than the secret number
#      *  0 if the number is equal to the secret number
#      *  1 if the number is greater than the secret number
#  
#     returns: integer, the secret number
#     ''' 
#    guess = 1
#     if isMyNumber(guess) == 0:
#         return guess
#     foundNumber = False
#     while not foundNumber:
#         sign = isMyNumber(guess)
#         if sign == 0:
#             return guess
#         elif sign == -1:
#             guess *= 2
#         elif sign==1:
#             guess -= 1
#     return guess 
# =====================================RINGUIN========================================
#print(jumpAndBackpedal(1)) #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# =============================================================================
# def Square(x):
#     return SquareHelper(abs(x), abs(x))
# 
# def SquareHelper(n, x):
#     if n == 0:
#         return 0
#     return SquareHelper(n-1, x) + x
# a=-3
# print(Square(a))
# print(a**a)
# 
# =============================================================================

# =============================================================================
# stuff  = "iQ"
# for thing in stuff:
#     if thing == 'iQ':
#         print("Found it")
# 
# =============================================================================

# =============================================================================
# def f(x):
#     while x > 3:
#         f(x+1)
# f(4)
# =============================================================================
# =============================================================================
# i=-1
# j=-1
# while i >= 0:
#     while j >= 0:
#         print(i, j)
# =============================================================================

# =============================================================================
# L= {'1':1, '2':2, '3':3}
# print(L)
# =============================================================================

# =============================================================================
# L = [1,2,3]
# d = {'a': 'b'}
# def f(x):
#     return 3
# #print(int('abc'))
# #print(d['b'])
# #for i in  range(1000001,-1,-2):
# #    print(f)
# =============================================================================
