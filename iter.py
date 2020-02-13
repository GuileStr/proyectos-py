# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:19:04 2020

@author: palar
"""

x = int(input("echa un num para iterarlo en si mismo: "))
ans= 0
itersleft=x
while itersleft!=0:
    ans+=x
    itersleft-=1
print(str(x)+ ' x ' +str(x) +' = ' + str(ans))