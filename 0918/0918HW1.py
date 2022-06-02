# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 21:40:59 2019

@author: Lynn
"""

W=input()
P=input()
Q=input()

W1=W
W2=W
W3=W
WS=W.split(' ')
W1S=W1.split(' ')
W2S=W2.split(' ')
W3S=W3.split(' ')
L=len(WS)
while(P in W1S):
    F1=W1S.index(P)
    W1S[F1]=Q
while(P in W3S):    
    W3S.remove(P)
Y={}
for i in range(L):    
    if(WS[i]==P):          
        Y[i]=1
    else:
        Y[i]=0
        
PT=0
for i in range(L):
    if(Y[i]==1):
        W2S.insert(PT,Q)
        PT=PT+1 
    
    PT=PT+1    
OP1=" ".join(W1S)    
OP2=" ".join(W2S)
OP3=" ".join(W3S)
print(OP1)
print(OP2)
print(OP3)