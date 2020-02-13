# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 09:24:33 2020

@author: palar
"""
# =============================================================================
# def oddTuples(aTup):
#     return aTup[::2]
# 
# q = tuple(map(int, input().rstrip().split()))
# print(oddTuples(q))
# 
# =============================================================================
 
x = (1, 2, (3, 'John', 4), 'Hi')
print(x[-1][2])

"""
te=()
t=(2,"jeje",3)
print(t[0])
t=t+(5,6)
print(t)
print(t[1:2])
"""
"""
def get_data(aTuble):
    nums=()
    word=()
    for t in aTuble:
        nums = nums+(t[0],)
        if t[1] not in word:
            word = word+ (t[1],)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_word = len(word)
    return (min_nums,max_nums,unique_word)

(small,large,word)=get_data(((1,'mine'),(3,'yours'),(5,'ours'),(7,'mine')))
"""
"""
x=1
y=2
(x,y)=(y,x)
print(x,y)
"""