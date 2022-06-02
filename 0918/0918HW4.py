# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 08:06:24 2019

@author: Lynn
"""

N=input()
B=input()
NS=N.split(' ')
BS=B.split('/')
FirstName=NS[0]
LastName=NS[1]
yyyy=BS[0]
mm=BS[1]
dd=BS[2]
print('{FirstName} is born at year {yyyy} month {mm} day {dd} in {LastName} family.'.format(FirstName=FirstName,yyyy=yyyy,mm=mm,dd=dd,LastName=LastName))