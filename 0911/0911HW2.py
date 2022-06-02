# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 23:25:32 2019

@author: Lynn
"""


import math
a=int(input())
b=int(input())
c=int(input())
s=math.sqrt(b*b-4*a*c)
x1=(-b+s)/(2*a)
x2=(-b-s)/(2*a)
print("%.1f"%x1)
print("%.1f"%x2)
