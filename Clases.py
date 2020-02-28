# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 12:06:27 2020

@author: palar
"""

class Coordinate(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance(self,other):
        x_diff_sq=(self.x-other.x)**2
        y_diff_sq=(self.y-other.y)**2
        return(x_diff_sq + y_diff_sq)**.05
        
c=Coordinate(3,4)

origin=Coordinate(0,0)

print(c.x)
print(origin.x)
#=========== Tanto "c", como "origin" son variables donde se instancia un objeto
#=========== por lo que se puede usar uso de los atributos del objeto con esas variables.
#=======Por ejemplo
print(c.distance(origin))
#========== Also, se puede hacer uso del objeti mismo mandando los dos parametros
print(Coordinate.distance(c,origin))
#==========En el primer caso no se manda, dado que c.distance hace referencia de que c equivale
#==========al primer parametro de distance... o más bien que va a formar parte del trabajo
print(c)