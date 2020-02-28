# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:59:19 2020

@author: palar
"""

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    def __eq__(self,other):
        return self.getX() ==other.getX() and self.getY() == other.getY()
    
    def __repr__(self):  #remove this and the next line and re-run
        return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'
    
a = Coordinate(0,0)
b= Coordinate(0,0)

print(a==b)