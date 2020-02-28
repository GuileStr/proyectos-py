# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 13:05:01 2020

@author: palar
"""

def dict_invert(d):
    new={}
    dV=list(d.values())
    dK=list(d.keys())
    l=[]
    print("Values",dV)
    print("Keys",dK)
    ndv=[]
    ndk=[]
    for i in dV:
        if i not in ndv:
            ndv.append(i)
    print("llaves nuevas totales",ndv)

    for i in d:
        ndk.append(i)
        
        
    for i in range(len(d)-1):
        new[ndv[i]]=ndk
    return new

d = {1: 1, 2: 1,3:4}
print(dict_invert(d))