# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 11:41:21 2020

@author: palar
"""

def minimumBribes(ent):
    m=0 #Movimientos
    size= len(ent) #Tamaño de entrada
    
    while size>0:
        last=ent[size-1]#While la entrada sea mayor a cero
        print("El utlimo ahora es",last)
        if size>1:
            print("comparando",last,"con",ent[last-1])
            if last<ent[last-1]:
                dif=abs(ent[last-1]-last)
                print("Ultimo",last)
                print("enfrete esta",ent[last-1])
                print("diferencia",dif)
                if dif==3:
                    print("Too chaotic")
                    break
                else:
                    m+=dif
        size-=1
    return int(m)


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))