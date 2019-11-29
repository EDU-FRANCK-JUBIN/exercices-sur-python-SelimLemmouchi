# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:20:09 2019

@author: Moi
"""

from pyDatalog import pyDatalog


pyDatalog.create_terms('factorial, N')

factorial[N] = N*factorial[N-1]
factorial[1] = 1

print(factorial[3]==N)