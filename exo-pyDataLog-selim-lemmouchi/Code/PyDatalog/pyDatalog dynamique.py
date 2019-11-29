# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 18:08:58 2019

@author: Moi
"""

from pyDatalog.pyDatalog import assert_fact, load, ask

# + parent(bill, 'John Adams')
assert_fact('parent', 'bill','John Adams') 


# specify what an ancestor is
load("""
    ancestor(X,Y) <= parent(X,Y)
    ancestor(X,Y) <= parent(X,Z) & ancestor(Z,Y)
""")


# prints a set with one element : the ('bill', 'John Adams') tuple
print(ask('parent(bill,X)')) 

