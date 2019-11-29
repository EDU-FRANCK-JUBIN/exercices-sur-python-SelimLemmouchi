# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:49:15 2019

@author: Moi
"""

from pyDatalog import pyDatalog
pyDatalog.create_terms('factorial, N')

factorial[N] = N*factorial[N-1] 
factorial[1] = 1

print(factorial[3]==N)


pyDatalog.create_atoms('salary', 'manager')

# John is the manager of Mary, who is the manager of Sam
+ (salary['John'] == 6800)

+ (manager['Mary'] == 'John')
+ (salary['Mary'] == 6300)


