# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 18:25:38 2019

@author: Moi
"""

from pyDatalog import pyDatalog
pyDatalog.create_terms('X,Y,Z, salary, tax_rate, tax_rate_for_salary_above, net_salary')
salary['foo'] = 60
salary['bar'] = 60

# Python equivalent
# _salary = dict()
# _salary['foo'] = 60
# _salary['bar'] = 110

# give me all the X and Y so that the salary of X is Y
print(salary[X]==Y)
print({X.data[i]:Y.data[i] for i in range(len(X.data))})        
# python equivalent
# print(_salary.items())

