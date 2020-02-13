# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 16:48:07 2020

@author: palar
"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    may=max(arr)
    sec=0
    for i in range(n):
        if  arr[i]==may:
            arr.remove(may)
            break
#            sec=arr[i]
    print(max(arr))

