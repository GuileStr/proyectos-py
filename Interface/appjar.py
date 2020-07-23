# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 13:05:38 2020

@author: palar
"""
from appJar import gui

# handle button events
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        print("User:", usr, "Pass:", pwd)

# create a GUI variable called app
app = gui("jeje", "400x200")
app.setBg("blue")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to the game")
app.setLabelBg("title", "black")
app.setLabelFg("title","red")

app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")

app.startLabelFrame("Simple", 0, 0)
app.addImage("Rodolfito", "rodolfo.png")
app.stopLabelFrame()

# link the buttons to the function called press
app.addButtons(["Submit", "Cancel"], press)

app.setFocus("Username")

# start the GUI
app.go()