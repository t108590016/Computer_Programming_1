# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 12:53:54 2019

@author: Lynn
"""
def WhoWin():
    IP={}
    ScoreA=0
    ScoreB=0
    for i in range(0,6):
        IP[i]=input()
        if i>2:
            if IP[i]=='J' or IP[i]=='Q' or IP[i] == 'K' :
                ScoreB+=0.5
            elif IP[i]=='A':
                ScoreB+=1
            else:
                ScoreB+=int(IP[i])
        else:
            if IP[i]=='J' or IP[i]=='Q' or IP[i] == 'K' :
                ScoreA+=0.5
            elif IP[i]=='A':
                ScoreA+=1
            else:
                ScoreA+=int(IP[i])
    if ScoreB > 10.5:
        ScoreB=0 
    if ScoreA > 10.5:
        ScoreA=0
    print(ScoreA)
    print(ScoreB)        
    if abs(ScoreA-10.5)<abs(ScoreB-10.5):
        print('A贏')
    elif abs(ScoreA-10.5)==abs(ScoreB-10.5):
        print('平手')
    else:
        print('B贏')
WhoWin()
        
