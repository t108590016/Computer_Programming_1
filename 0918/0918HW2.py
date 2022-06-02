# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 20:07:26 2019

@author: Lynn
"""
#A="This is a book"
#B="That is a cat"
#x="is"
#y="was"
A=input()
B=input()
x=input()
y=input()
C=A+B
D=C.replace(x,y)
E=D[:3]+D[-3::1]
#print(len(C))
#print(len(D))
print(len(C)+len(D))
print(E*3)