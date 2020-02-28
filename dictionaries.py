# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:57:37 2020

@author: palar
"""

# =============================================================================
# a = 'Mary&Johnmary&JohnMaRy&joHn'
# print(a)
# print(a.lower())
# print(a.lower().count('mary'))
# =============================================================================

animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}
animals['d'] = 'donkey'
animals['a'] = 'anteater'
del animals['b']
print(animals.values())


# =============================================================================
# def lyrics_to_frequencies(lyrics):
#     myDic = {}
#     for word in lyrics:
#         if word in myDic:
#             myDic[word]+=1
#         else:
#             myDic[word]=1
#     return myDic
# 
# def most_common_words(freq):
#     values = freq.values()
#     best=max(values)
#     word=[]
#     for k in freq:
#         if freq[k]==best:
#             word.append(k)
#     return (word,best)
# 
# def words_often(freqs,minTimes):
#     result=[]
#     done=False
#     while not done:
#         temp = most_common_words(freqs)
#         if temp[1] >= minTimes:
#             result.append(temp)
#             for w in temp[0]:
#                 del(freqs[w])
#         else:
#             done=True
#     return result
# =============================================================================
