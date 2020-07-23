# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 17:28:18 2020

@author: palar
"""

from appJar import gui

def enter(wdgt): 
    print("IN", wdgt)
def leave(wdgt):
    print("OUT", wdgt)

app=gui("jiji")
app.addLabel("l1", "Testing...")
app.setLabelSubmitFunction("l1", [enter, leave])
app.go()