# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 12:39:14 2020

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
    
class MITPerson(Person):
    nextIdNum = 0 # next ID number to assign

    def __init__(self, name):
        Person.__init__(self, name) # initialize Person attributes
        # new MITPerson attribute: a unique ID number
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    # sorting MIT people uses their ID number, not name!
    def __lt__(self, other):
        return self.idNum < other.idNum
        
    def speak(self, utterance):
        return (self.name + " says: " + utterance)
        
class Proffesor(Person):
    def __init__(self,name,departament):
        MITPerson.__init__(self,name)
        self.departament=departament
    def speak(self,utterance):
        new='In course'+self.departament+' we say '
        return MITPerson.speak(self,new+utterance)
    def lecture(self,topic):
        return self.speak('it is obvious that' + topic)
        
p1 = MITPerson('Eric')
p2 = MITPerson('John Guttag')
p3 = MITPerson('John Smith')
p4 = Person('John')

prfR=Proffesor('IS Ricardo','python')
print(prfR.speak('Raul is joto '))