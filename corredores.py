# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 15:02:51 2020

@author: palar
"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    may=max(arr)
    v=0
  
    sec=0
    for i in range(n):
        if may==arr[i]:
            v= arr[i]
            #arr.remove(max(arr))
    arr.remove(v)
    sec=max(arr)
    print(sec)
