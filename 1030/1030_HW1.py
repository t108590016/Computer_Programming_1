# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:08:22 2019

@author: Lynn
"""

def function():
    N=input().split(' ')
    Nodd=list()
    Neven=list()
    Nop=list()
    j=w=0
    for i in range(0,len(N)):
        if int(N[i])%2==1:
            Neven.append(int(N[i]))
            j+=1
        else:
            Nodd.append(int(N[i]))
            w+=1
    Nodd.sort(reverse=True)
    Neven.sort()
    Nop=Nop+Neven+Nodd
    print(Nop)
    
function()    