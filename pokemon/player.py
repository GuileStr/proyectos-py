# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 03:04:12 2020

@author: palar
"""

class player(object):
    def __init__(self, name):
        inventory=[]
        self.name = name
        self.inv=inventory
    def __str__(self):
        return 'The player is: '+str(self.name)+ ' and his inventory is: '+str(self.inv)
    def fillInv(self, item):
        if item not in self.inv:
            self.inv.append(item)
        else:
            print('Only one of '+item+'(in the inventory at once) allowed')
    def useItem(self,itemU):
        try:
            print('You used '+str(self.inv[itemU]))
            self.inv.pop(itemU)
        except:
            print('You dont have that item')
    
    

pl=player('Ringo')
print('new player:')
print(pl)
print('Giving him an item pokewebo and print')
pl.fillInv('pokewebo')
print(pl)

print('Using an item with its index')
pl.useItem(0)
print(pl)
