# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:15:53 2020

@author: palar
"""

class fraction(object):
    def __init__(self,numer,denom):
        self.numer=numer
        self.denom = denom
    def __str__(self):
        return str(self.numer)+'/'+str(self.denom)
    def getNumber(self):
        return self.numer
    def getDenom(self):
        return self.denom
    def __add__(self,other):
        numerNew = other.getDenom()*self.getNumber() \
                    + other.getNumer() * self.getDenom()
        denomNew = other.getDenom()*self.getDenom()
        return fraction(numerNew,denomNew)
    def __sub__(self,other):
        numerNew=other.getDenom()*self.getNumer() \
                   + other.getNumer()* self.getDenom()
        denomNew= other.getDenom()*self.getDenom()
        return fraction(numerNew,denomNew)
    def convert(self):
        return self.getNumber()/self.getDenom()