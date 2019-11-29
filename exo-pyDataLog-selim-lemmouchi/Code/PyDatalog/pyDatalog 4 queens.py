# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 19:05:46 2019

@author: Moi
"""
from pyDatalog import pyDatalog
pyDatalog.create_terms('queens,next_queen,ok,X0,X1,X2,X3')

# give me the solution to the 4-queen problem

queens(X0,X1,X2,X3) <= queens(X0,X1,X2) & next_queen(X0,X1,X2,X3)
queens(X0,X1,X2)    <= queens(X0,X1)    & next_queen(X0,X1,X2)
queens(X0,X1)       <= queens(X0)       & next_queen(X0,X1)
queens(X0)          <= (X0._in(range(4)))

next_queen(X0,X1,X2,X3) <= next_queen(X1,X2,X3) & ok(X0,3,X3)
next_queen(X0,X1,X2)    <= next_queen(X1,X2)    & ok(X0,2,X2)
next_queen(X0,X1)       <= queens(X1)           & ok(X0,1,X1)

ok(X1, N, X2) <= (X1 != X2) & (X1 != X2+N) & (X1 != X2-N)

print(queens(X0,X1,X2,X3))