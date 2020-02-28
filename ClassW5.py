# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 09:31:06 2020

@author: palar
"""
import datetime

class Person(object):
    def __init__(self,name):
        """create a person called name"""
        self.name= name
        self.birthday=None
        self.lastName= name.split(' ')[-1]
    def __lt__(self,other):
        if self.lastName==other.lastName:
            return self.name<other.name
        return self.lastName<other.lastName
    def setBirthday(self,month,day,year):
        self.birthday=datetime.date(year,month,day)
    def getAge(self):
        if self.birthday==None:
            raise ValueError
        return(datetime.date.today()-self.birthday).days
    def getLastName(self):
        return self.lastName
    def __str__(self):
        return self.name
    
r=Person('Ricardo Reyes')
r.setBirthday(10,11,1997)
print(r.getLastName())
print(r.getAge())