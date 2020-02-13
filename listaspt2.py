# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:13:25 2020

@author: palar

"""
def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

print(applyEachTo([inc, max, int], -3))









# =============================================================================
# def lposxlpos(L):
#     for i in range(len(L)):
#         L[i]=L[i] * L[i]
#     return L
# lposxlpos(testList)
# 
# =============================================================================

# =============================================================================
# # Your Code Here
# def absoluteEach(L):
#     for i in range(len(L)):
#          L[i]= abs(L[i])
#     return L
# absoluteEach(testList)
# =============================================================================


# =============================================================================
# 
# #[1, -4, 8, -9]
# # Your Code Here
# def listPlusOne(L):
#     for i in range(len(L)):
#          L[i]= L[i]+1
#     return L
# listPlusOne(testList)
# =============================================================================
# =============================================================================
# 
# aList = [0, 1, 2, 3, 4, 5]
# bList = aList
# aList[2]='hello'
# #print(bList)
# 
# cList = [6, 5, 4, 3, 2]
# dList = []
# for num in cList:
#     dList.append(num)
# cList[2]=20
# print(dList)
# =============================================================================

# =============================================================================
# def applyToEach(L,f):
#     for i in range(len(L)):
#         L[i]= f(L[i])
# 
# L=[1,-2,3.4]        
# applyToEach(L,abs)
# applyToEach(L,int)
# #applyToEach(L,fact)
# =============================================================================
# =============================================================================
# def applyToEach(L, f):
#     for i in range(len(L)):
#         L[i] = f(L[i])
# testList = [1, -4, 8, -9]
# print(applyToEach(testList,int))
# =============================================================================
