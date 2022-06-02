# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:30:52 2019

@author: Lynn
"""
def function():
    n=int(input())
    xCovered={}
    xs={}
    for w in range(0,n):
        x=input()
        xs=x.split(' ')
        x1=int(xs[0])
        x2=int(xs[1])
        for i in range(x1,x2):
            xCovered[i]=1
    print(len(xCovered))
function()


