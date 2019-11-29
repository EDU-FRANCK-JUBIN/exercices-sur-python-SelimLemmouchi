# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 18:01:54 2019

@author: Moi
"""

from pyDatalog import pyDatalog, Logic
Logic() # initializes the pyDatalog engine


Logic() # creates an empty set of clauses for use in the current thread
# add first set of clauses here
first = Logic(True) # save the current set of clauses in variable 'first'

Logic() # first is not affected by this statement
# define the second set of clauses here
second = Logic(True) # save it for later use

Logic(first) # now use first in the current thread
# queries will now run against the first set of rules

