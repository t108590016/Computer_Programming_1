# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 21:34:35 2019

@author: Lynn
"""

n=int(input())
def function(n):
    for i in range(0,n):
        print('#'*(n+i),end='')
        for j in range(n-i,0,-1):
            print(j,end='')
        print('')
function(n)        
