# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:31:20 2019

@author: Lynn
"""
def a():
    m=int(input())
    n=int(input())
    sum1=0
    sum2=1
    for i in range(m,n+1,2):
        sum1=sum1+i
    for i in range(m,n+1,3):
        sum2=sum2*i
    print(sum1)
    print(sum2)
a()