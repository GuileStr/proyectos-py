# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 12:11:37 2020

@author: palar
"""

def minimumBribes(q):
    size = len(q)
    m=0
    while size>=0:
        if (q[size-1]-size)>2:
            return "Too chaotic"
        else:
            m+=2
    
if __name__ == '__main__':
    t = int(input())
    
    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)