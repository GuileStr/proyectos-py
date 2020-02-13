# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 14:36:30 2020

@author: palar
"""

# =============================================================================
# x = [1, 2, [3, 'John', 4], 'Hi'] 
# x[0]=8
# x.extend([4, 1, 6, 3, 4])
# x.pop(4)
# print(x)
# =============================================================================


listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']
listA.sort()
listA.insert(0,100)
listA.remove(3)
listA.append(7)
listB.sort()
listB.pop()
listA.extend([4, 1, 6, 3, 4])
print(listA.pop(4))

"""
lista=[1,2]
lista.insert(0,100)
lista.remove(2) 
print(lista)
"""
#lisa=['x', 'z', 't', 'q']
#lisa.sort()
#lisa.pop()
#print(lisa.remove('a'))