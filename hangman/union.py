# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:32:11 2020

@author: palar
"""
def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return 1
   else:
      return n * f(n-1)
  
print(f(3))
# =============================================================================
# def union(set1, set2):
#    """
#    set1 and set2 are collections of objects, each of which might be empty.
#    Each set has no duplicates within itself, but there may be objects that
#    are in both sets. Objects are assumed to be of the same type.
# 
#    This function returns one set containing all elements from
#    both input sets, but with no duplicates.
#    """
#    if len(set1) == 0:
#       return set2
#    elif set1[0] in set2:
#       return union(set1[1:], set2)
#    else:
#       return set1[0] + union(set1[1:], set2)
#   
# print(union('c','ab'))
# =============================================================================

# =============================================================================
# def foo(x, a):
#    """
#    x: a positive integer argument
#    a: a positive integer argument
# 
#    returns an integer
#    """
#    count = 0
#    while x >= a:
#       count += 1
#       x = x - a
#    return count
# 
# print(foo(10,3))
# =============================================================================
# =============================================================================
# def rem(x, a):
#     """
#     x: a non-negative integer argument
#     a: a positive integer argument
# 
#     returns: integer, the remainder when x is divided by a.
#     """
#     if x == a:
#         return 0
#     elif x < a:
#         return x
#     else:
#         return rem(x-a, a)
# 
# u=7
# d=5
# print(rem(u,d))
# print(u%d)
# 
# =============================================================================
