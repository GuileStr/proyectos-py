# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:57:52 2020

@author: palar
"""

count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print("Iteration " + str(iteration) + "; count is: " + str(count))