# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 10:29:27 2020

@author: palar
"""
def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3)


#def foo(x, y = 5):
#   def bar(x):
#      return x + 1
#   return bar(y * 2)
          
print(foo(5))

#def a(x, y, z):
#     if x:
#         return y
#     else:
#         return z

#def b(q, r):
#    return a(q>r, q, r)
#print(a(False,2,3))



#def a(x):
#   '''
#   x: int or float.
#   '''
#   return x + 1

#def b(x):
#   '''
#   x: int or float.
#   '''
#   return x + 1.0
  
#def c(x, y):
#   '''
#   x: int or float. 
#   y: int or float.
#   '''
#   return x + y

#def d(x, y):
#   '''
#   x: Can be of any type.
#   y: Can be of any type.
#   '''
#   return x > y

#def e(x, y, z):
#   '''
#   x: Can be of any type.
#   y: Can be of any type.
#   z: Can be of any type.
#   '''
#   return x >= y and x <= z

#def f(x, y):
 #  '''
 #  x: int or float.
 #  y: int or float
 #  '''
 #  x + y - 2
#
#
#print(f)