# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:50:38 2019

@author: Lynn
"""
def function():
    n=int(input())
    numbers={}
    for i in range(0,n):
        numbers[i]=int(input())
    for i in range(0,n-1):
        for j in range(i+1,n):
            if numbers[i]<numbers[j]:
                t=numbers[i]
                numbers[i]=numbers[j]
                numbers[j]=t
    print(numbers[1])    
    print(numbers[0]*numbers[n-1])

function()
