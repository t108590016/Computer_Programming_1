# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 21:58:04 2019

@author: Lynn
"""

a=int(input())
b=int(input())
def function(a,b):
    total=0
    if a%2==1:
        a+=1
    for i in range(a,b+1,2):
        total+=i
    print(total)
function(a,b)