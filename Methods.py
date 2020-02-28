# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 12:28:17 2020

@author: palar
"""
class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x 
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8
w1 = Weird(X, Y)
w2 = Wild(X, Y)
w3 = Wild(17, 18)
w4 = Wild(X, 18)
X = w4.getX() + w3.getX() + w2.getX()
Y = w4.getY() + w3.getY()
Y = Y + w2.getY()
print(w2.getY())
# ==========================NOMBRE DE ATRIBUTOS CON ACCION===================================================
# __add__(self,other) -> self + other
# __sub__(self,other) -> self - other
# __eq__(self,other) -> self == other
# __lt__(self,other) -> self < other
# __len__(self) -> len(self) 
# __str__(self) -> print(self)
# =============================================================================
# ========================FIRST CASE=====================================================
# class Clock(object):
#     def __init__(self, time):
#         self.time = time
#     def print_time(self):
#     	time = '6:30'
#     	print(self.time)
# 
# clock = Clock('5:30')
# clock.print_time()
# =========================FIRST CASE====================================================
# =========================SECOND CASE====================================================
# class Clock(object):
#     def __init__(self, time):
#         self.time = time
#     def print_time(self, time):
#         print(time)
# 
# clock = Clock('5:30')
# clock.print_time('10:30')
# =========================SECOND CASE====================================================
