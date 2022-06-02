# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 21:28:28 2019

@author: Lynn
"""
def main():
    x=input()
    n=int(input())
    if x=='1':
        function1(n)
    elif x=='2':
        function2(n)
    else:
        function3(n)
def function1(n):
    x=int(n/2)+1
    for i in range(0,x):
        print('*'*(i+1))
    for i in range(x-1,0,-1):
        print('*'*i)
    
def function2(n):
    x=int(n/2)+1
    for i in range(0,x):
        print('.'*(x-i-1),end='')
        print('*'*(i+1))
    for i in range(x-1,0,-1):
        print('.'*(x-i),end='')
        print('*'*i)
        
def function3(n):
    for i in range(1,n+1,2):
        print('.'*(int(n/2)-int(i/2)),end='')
        print('*'*i)
    for i in range(n-2,0,-2):
        print('.'*(int(n/2)-int(i/2)),end='')
        print('*'*i)
main()