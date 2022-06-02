# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:20:45 2019

@author: Lynn
"""
def BMI():
    Name=input()
    H=float(input())/100
    W=float(input())
    bmi=round(W/H/H,6)
    if bmi>24:
        print('Hi {0}, Your BMI: {1} too HIGH.'.format(Name,bmi))
    elif bmi>18.5:
        print('Hi {0}, Your BMI: {1}.'.format(Name,bmi))    
    else:
        print('Hi {0}, Your BMI: {1} too LOW.'.format(Name,bmi))
BMI()
    
    