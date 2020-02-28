# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:27:20 2020

@author: palar
"""

class Animal(object):
    def __init__(self,age):
        self.age=age
        self.name=None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self,newage):
        self.age=newage
    def set_name(self,newname):
        self.name=newname
    def __str__(self):
        return 'animal: '+str(self.name)+':'+str(self.age)
    
a=Animal(1)
a.set_name('Livan')
# a.get_name() == Animal.getName(a)
print(a.name)
print(a.get_name())
print(a)