# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 21:41:28 2019

@author: Lynn
"""
DiscountList=[[1,0.95,0.9,0.8],[1,0.9,0.85,0.75],[1,0.85,0.8,0.8]]
OriginPrice=[30,70,40]
Quantity={}
Discount={}
for i in range(0,3):
    Quantity[i]=int(input())
for i in range(0,3):
    if Quantity[i] > 20:
        Discount[i]=DiscountList[i][3]
    elif Quantity[i] > 15:
        Discount[i]=DiscountList[i][2]    
    elif Quantity[i] > 10:
        Discount[i]=DiscountList[i][1]  
    else:
        Discount[i]=DiscountList[i][0]
TotalPrice=0
TotalQuantity=0
for i in range(0,3):
    M=Quantity[i]*OriginPrice[i]*Discount[i]
    TotalPrice=TotalPrice+M
    TotalQuantity=TotalQuantity+Quantity[i]
if TotalQuantity >= 30:
    TotalPrice = TotalPrice * 0.87
print(int(round(TotalPrice,0)))


    