# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:36:18 2020

@author: palar
"""

def ispal(s):
    def toChar(s):
        s=s.lower()
        ans=''
        for c in s:
            if c in 'abcdefghyjklmnopqrstuvxyz':
                ans=ans+c
        return ans
    
    def isPali(s):
        if len(s)<=1:
            return True
        else:
            return s[0]==s[-1] and isPali(s[1:-1])
    return isPali(toChar(s))

print(ispal('anita lava la tina'))