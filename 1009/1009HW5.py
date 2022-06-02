# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 22:19:25 2019

@author: Lynn
"""
n=int(input())
def function(n):
    total=1
    for i in range(n,0,-1):
        total=total*i
    print(total)   
function(n)
