# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 00:11:47 2020

@author: palar
"""
import random
wness={"awa":"yerba","fuebo":"awa","yerba":"fuebo"}
class pet(object):
    def __init__(self, name, hp,typ,attacks):
        self.name=name
        self.level=1
        self.xp=0
        self.xpNeeded=100
        self.status="alive"
        self.hp=hp
        self.hpMax=hp
        self.typ=typ
        self.attacks=attacks

    def __str__(self):
        return "Pet: "+str(self.name)+", status: "+str(self.status)+", with "+str(self.hp)+"/"+str(self.hpMax)
    
    
    def beingHurt(self,dmg,ty,attname):
        damage=dmg
        wkn=wness[self.typ]
        if wkn==ty:
            damage=damage*2
            self.hp=self.hp-damage
            return str(attname)+" was super efective and cause "+str(damage)+" of damage"
        else:
            self.hp=self.hp-damage
            return str(attname)+" hits and causes "+str(damage)+" of damage"
    def beingHealed(self,heal):
        self.hp+=heal
        
        return str(self.name)+" was healed "+str(heal)+" of hp"
    
    def winXp(self,wxp):
        self.xp+=wxp
        if self.xp>=self.xpNeeded:
            self.level+=1
            self.xp=0
            self.xpNeeded=+42
            return str(self.name)+" gets "+str(wxp)+" and gets a level up"
        else:
            return str(self.name)+" gets "+str(wxp)

def calculateXpp(winnerlvl,loserlvl):
    exp=0
    difference= winnerlvl-loserlvl
    if 0>=abs(difference)<=10:
        exp=10
        
    elif 11>=abs(difference)<=20:
        exp=15
    return exp

def playTheGame(pka,pkb):
    print("Se armaron los wamasos")
    while True:
        if pka.hp==0:
            print(str(pka.name)+" was defeated by "+str(pkb.name))
            wxp=calculateXpp(pkb.level, pka.level)
            print(str(pkb.name)+" gets "+str(wxp)+" of hp")
            pkb.winXp(wxp)
            break
        
        elif pkb.hp==0:
            print(str(pkb.name)+" was defeated by "+str(pka.name))
            wxp=calculateXpp(pka.level, pkb.level)
            print(str(pka.name)+" gets "+str(wxp)+" of xp")
            pka.winXp(wxp)
            break
        
        print(pka)
        print(pkb)
        choose=int(input("[1] attack\n[2] exit \nYour choose: "))
        if choose==1:
            atname=list(pka.attacks.keys())[0]
            print(pkb.beingHurt(10, pka.attacks[atname], atname))
            pkbChoose = random.randint(0,1)
            if pkbChoose==0:
                print("enemy skips its turn")
            else:
                print("enemy uses an attack")
                atnameDos=list(pkb.attacks.keys())[0]
                print(pka.beingHurt(10,pkb.attacks[atnameDos],atnameDos))
        elif choose==2:
            break
        else:
            print("Invalid choose")
        
    print("The game reached the end")
    
pka = pet("Lola",100,"fuebo",{"scratch":"normal","fang":"fuebo"})
pkb = pet("Zorro",100,"awa",{"bite":"normal","shot":"awa"})
#print(pka.attacks["scratch"])
print("Welcome to the bet battle event")
print("The player(You... or pka; in this case Lola ) will always start the battle")
playTheGame(pka, pkb)