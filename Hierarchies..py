# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:35:53 2020

@author: palar
"""
import random
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
    
class Cat(Animal):
    def speak(self):
        print('meow')
    def __str__(self):
        return 'cat: '+str(self.name)+':'+str(self.age)

class Person(Animal):
    def __init__(self,name,age):
        Animal.__init__(self,age)
        Animal.set_name(self,name)
        self.friends=[]
    def get_friends(self,fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("Hello")
    def age_diff(self,other):
        diff=self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name,'is',diff,'years older than',other.name)
        else:
            print(self.name,'is',-diff,'years younger than',other.name)
    def __str__(self):
        return 'person: '+str(self.name)+":"+str(self.age)
class Rabbit(Animal):
    tag=1
    def __init__(self,age,paretn1=None,parent2=None):
        Animal.__init__(self,age)
        self.paretn1=paretn1
        self.parent2=parent2
        self.rid= Rabbit.tag
        Rabbit.tag+=1
    def get_rid(self):
        return str(self.rid).zfill(3)
    def get_paretn1(self):
        return self.paretn1
    def get_parent2(self):
        return self.parent2
            
    
class Student(Person):
    def __init__(self,name,age,major=None):
        Person.__init__(self,name,age)
        self.major=major
    def change_major(self,major):
        self.major=major
    def speak(self):
        r=random.random()
        if r<0.25:
            print('i have homework')
        elif 0.25<=r<0.5:
            print("i need some sleep")
        elif 0.5<=r<0.75:
            print("i should eat")
        else:
            print("i am watching tv")
    def __str__(self):
        return 'student:'+str(self.name)+":"+str(self.age)+":"+str(self.major)
    
coneji=Rabbit(3)
coneji.set_name('Franky')
jumps=Rabbit(3)
jumps.set_name('Awacate')
euc=Rabbit(1,coneji,jumps)
euc.set_name('Eucalipto')
print(coneji)
print(jumps)
print(euc.get_paretn1)
# =============================================================================
# ric=Person('Ringuin',23)
# erika=Student('Erika',19,'ISW')
# print(ric)
# print(erika)
# =============================================================================
