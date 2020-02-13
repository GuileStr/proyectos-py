# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 14:01:40 2020

@author: palar
"""

def minimumBribes(Q):
    moves = 0  # numero de movimientos
    Q = [P-1 for P in Q] #Este compa nos regresa las posiciones como deberian ir
    #ej: [2,1,5,3,4] => [1,0,4,2,3] = Q
    #print(Q)
    for i,P in enumerate(Q):
        # P es la posicion original
        # P en caso de ejemplo = 
        # P en iteracion 0 = 2 pero su posicion es 1
        # P en iteracion 1= 1 pero su posicion es 0
        # P en iteracion 2= 5 pero su posicion es 4
        # Etcetera xd || Entonces sabemos que son los valores uno por uno en Q
        # i es el numero pues original 1, 2, 3, 4, 5 segun se itere este rollo
        # (P-i) 
        # Más bien la diferencia de P(Pos original) y la actual i()
        # Entonces en la condicion vemos si:
        # P = 1 menos i = 0 [En la primer iteracion] = X
        # X es o bien si va ahí y no incrementa los moviemientos,
        # Si lo movieron para atras (-1) y tampoco es movimiento sumado
        # Si es un resultado 1 o 2, es que se movio adelante una o dos veces
        # O bien, significa que salto demás
        
        #ej: 2 1 5 3 4
        # 2 dio un paso enfrente = 1
        # 1 dio uno atras        =-1
        # 5 dio dos enfrente     = 2
        # 3 dio uno atras        =-1
        # 4 dio uno atras        =-1
        if P - i > 2:
            print("Too chaotic")
            return
        for j in range(max(P-1,0),i):
           # print("j=",j)
           # print("Q[j]=",Q[j])
            if Q[j] > P:
                moves += 1
    print(moves)
    
if __name__ == '__main__':
    t = int(input())
    
    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)