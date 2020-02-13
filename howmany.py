# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:46:29 2020

@author: palar
"""
    ## global var
    
# ==FIBONACCI============================================================
# def fib(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 2
#     else:
#         return fib(n-1) + fib(n-2)
#     
# def fib_efficient(n,d):
#     if n in d:
#         return d[n]
#     else:
#         ans =fib_efficient(n-1,d) + fib_efficient(n-2,d)
#         d[n]= ans
#         return ans
#     
# =============================================================================
# =============================================================================
# def biggest(aDict):
#     '''
#     aDict: A dictionary, where all the values are lists.
# 
#     returns: The key with the largest number of values associated with it
#     '''
#     # Your Code Here
#     x=0
#     l=''
# #print(animals.keys())
#     for i in animals.keys():
#          if len(animals[i])>x:
#              x=len(i)
#              l=i
#     return l
# =============================================================================



# =============================================================================
# def how_many(aDict):
#     '''
#     aDict: A dictionary, where all the values are lists.
# 
#     returns: int, how many values are in the dictionary.
#     '''
#     # Your Code Here
#     x=0
#     for i in aDict.values():
#         #print(i)
#         x+= len(i)
#     return (x)
#     
# =============================================================================
    


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(biggest(animals))
#x=0
#l=''
#print(animals.keys())
#for i in animals.keys():
         #print(i)
         #print(animals[i])
         #print(len(animals[i]))
         #x+= len(i)
#         if len(animals[i])>x:
#             x=len(i)
#             l=i
#print("el mas grande es "+l)



# =============================================================================
# print(len(animals['a']))
# print(len(animals))
# print(animals.values())
# x=0
# for i in animals.values():
#     print(i)
#     x+= len(i)
# print(x)
# =============================================================================
