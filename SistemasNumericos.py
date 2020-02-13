# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 09:35:44 2020

@author: palar
"""
def print_formatted(number):
    dec=0
    octa=0
    Hexa=0
    Bin=0
    for i in range(number):
        print(i+1)
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)