# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 21:26:03 2019

@author: Lynn
"""

def function():
    ip=input()
    ips=ip.split(' ')
    a1=int(ips[0])
    an=int(ips[1])
    d=int(ips[2])
    sum=0
    x=a1
    while x<=an:
        print(x,end='')
        if x<an:
            print(' ',end='')
        sum+=x
        x+=d
    print()
    print(sum)
function()