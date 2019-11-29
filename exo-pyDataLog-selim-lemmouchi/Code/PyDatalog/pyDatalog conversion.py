# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 19:08:25 2019

@author: Moi
"""

from pyDatalog import pyDatalog
from pyDatalog.pyDatalog import create_terms as terms
from pyDatalog.pyDatalog import ask

pyDatalog.create_terms('scale,A, B, C, V') # the long way of doing it

scale['meter', 'inch'] = 39.3700787
scale['mile', 'inch'] = 63360.0
scale['feet', 'inch'] = 12.0

scale[A, B] =  1/scale[B, A]
scale[A,B] = scale[A,C] * scale[C, B]

print(scale['inch', 'meter'] == V)
print(scale['mile', 'meter'] == V)

terms('conv')
conv[V, A, B] = V * scale[A, B]
print(conv[3, 'mile', 'meter'] == V)
print(conv[1, 'meter', 'feet'] == V)

