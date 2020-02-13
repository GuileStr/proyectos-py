# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 16:07:21 2020

@author: palar
"""

s = 'azcbobobegghaklboboasdboasidnoasbdboobdobasdoasbobobobobobb'
u=0
d=3
word=''
con=0
conbob=0
while d<len(s)-1:
    for char in s[u:d]:        
        word+=char
        con+=1
        if con==3:
            #print(word)
            if word=='bob':
                conbob+=1
    d+=1
    u+=1
    word=''
    con=0
print(conbob)