# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 17:57:40 2019

@author: Moi
"""

pyDatalog.create_terms('X,Y, quacks, input')
quacks(X) <= (input('Does a '+X+' quack ? (Y/N) ')=='Y')



pyDatalog.create_terms('print')
ok(X) <= (0 < X) & (Y==print(X))


import logging
from pyDatalog import pyEngine
pyEngine.Logging = True
logging.basicConfig(level=logging.INFO)

