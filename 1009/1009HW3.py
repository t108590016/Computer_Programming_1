# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 21:51:31 2019

@author: Lynn
"""

n=int(input())

def function(n):
    x=0
    for i in range(2,n):
        if n%i==0:
            x+=1
    if x>0:
        print('{0} is not prime number'.format(n))
    else:
        print('{0} is prime number'.format(n))
            
function(n)
