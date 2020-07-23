# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 17:18:46 2020

@author: palar
"""

from appJar import gui

def press(btn):
    print(btn)


app =  gui("My first GUI with appJar")

app.setBg('yellow')
app.setFg('orange')
app.setFont(15)

app.addLabel('title','Ola k ase?',press)
app.addButton('Erika shula',press)


app.go()