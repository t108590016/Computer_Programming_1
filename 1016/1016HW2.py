# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:37:58 2019

@author: Lynn
"""
def function():
    ips={}
    while(1):
        ip=input()
        if ip=='-1':
            break
    
        else:
            ips=ip.split(' ')    
            h=float(ips[0])
            w=float(ips[1])
            bmi=round(w/h/h,2)
            if (h<0.5 or h>2.5) :
                print("Input Error 0.5~2.50")
            elif (w<20 or w>300):
                print("Input Error 20~300")
            elif bmi<18.5:
                print("BMI too low")
            elif bmi>24:
                print("BMI too hight")
            else:
                print(bmi)
function()