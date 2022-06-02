# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 20:06:09 2019

@author: Lynn
"""
def function():
    ss={}
    s=input()
    ss=s.split(' ')
    x1=int(ss[0])
    y1=int(ss[1])
    x2=int(ss[2])
    y2=int(ss[3])
    x3=int(ss[4])
    y3=int(ss[5])
    n=0
    while(1):
        if((n-y1)%x1==0 and (n-y2)%x2==0 and (n-y3)%x3==0):
            print(n)
            break
        else:
            n=n+1
function()