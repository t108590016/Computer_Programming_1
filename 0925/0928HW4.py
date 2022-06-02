# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 14:26:21 2019

@author: Lynn
"""
def Cheapest():
    DollarPerSecond=[[0.08,0.1393,0.1349,1.1287,1.4803],[0.07,0.1304,0.1217,1.1127,1.2458],[0.06,0.1087,0.1018,0.9572,1.1243]]
    Discount=[183,383,983]
    quantity={}
    m={}
    Total={}
    t=0
    for i in range(0,5):
        quantity[i]=int(input())
    for i in range(0,3):
        for j in range(0,5):
            m[j]=DollarPerSecond[i][j]*quantity[j]
            t=t+m[j]
            m[j]=0
        Total[i]=t
        t=0
        if Total[i]<Discount[i]:
            Total[i]=Discount[i]
    min=0
    for i in range(0,3):
        if min == 0:
            min=Total[i]
            Cheapest=Discount[i]
        elif min>Total[i]:
            min=Total[i]
            Cheapest=Discount[i]
    print(str(Cheapest)+'型')  
      
Cheapest()