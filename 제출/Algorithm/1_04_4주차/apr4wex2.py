# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:33:43 2020

@author: 76619
"""


a = [10, 65, 100, 30, 95]
sum1 = 0
for a1 in a:
    if a1<40:
        sum1 +=40
    else:
        sum1 +=a1

print(int(sum1/len(a)))
