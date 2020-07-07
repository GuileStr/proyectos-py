# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 07:19:17 2020

@author: palar
"""
wness={"awa":"yerba","fuebo":"awa","yerba":"fuebo"}
class drogamonmon(object):
    def __init__(self, name, hp,typ,attacks):
        self.name=name
        self.status="alive"
        self.hp=hp
        self.typ=typ
        self.attacks=attacks

    def __str__(self):
        return "Drogamonmon: "+str(self.name)+", status: "+str(self.status)
    def beingHurt(self,dmg,ty,attname):
        damage=dmg
        wkn=wness[self.typ]
        if wkn==ty:
            damage=damage*2
            return str(attname)+" was super efective and cause "+str(damage)+" of damage"
        else:
            return str(attname)+" hits and causes "+str(damage)+" of damage"
            
    
new=drogamonmon("pishi",100,"awa",{"tackle":"normal","shot":"awa"})
print(new.beingHurt(10, "yerba", "Angry leaf"))
print(new.beingHurt(10, "awa", "Forced shower"))