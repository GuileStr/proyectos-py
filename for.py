# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 21:26:07 2020

@author: palar
"""

a=["zamudio","rivas","reyes","ramirez","lopez","leal","simental"]
b=[]
count=1
for i in sorted(a):
    tmp=str(count)+" "+i
    b.append(tmp)
    count+=1
    
print(b)