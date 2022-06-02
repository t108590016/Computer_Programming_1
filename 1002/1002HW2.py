# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:36:06 2019

@author: Lynn
"""
def UpperOrLower():
    S=input()
    UpperQuantity=0
    LowerQuantity=0
    for i in range(0,len(S)):
        if S[i].islower():
            print(S[i],end='')
            LowerQuantity+=1
        elif S[i].isupper():
            UpperQuantity+=1
    if(LowerQuantity>0):
        print('')
    else:
        print('No lowercase letters')
    print(len(S))
    print(UpperQuantity)
UpperOrLower()
        