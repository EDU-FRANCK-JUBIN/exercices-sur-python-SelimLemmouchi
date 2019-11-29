# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 13:38:43 2019

@author: Moi
"""


from pyDatalog import pyDatalog

pyDatalog.load("""
    # bill is the parent of John Adams
    + parent(bill,'John Adams') 
""")


# bill is the parent of John Adams
pyDatalog.assert_fact('parent', 'bill','John Adams') 




from pyDatalog import pyDatalog
pyDatalog.create_terms('X,Y,manager, count_of_direct_reports')

# the manager of Mary is John
+(manager['Mary'] == 'John')
+(manager['Sam']  == 'Mary')
+(manager['Tom']  == 'Mary')



# prints a set with one element : the ('bill', 'John Adams') tuple
print(pyDatalog.ask('parent(bill,X)')) 



# specify what an ancestor is
pyDatalog.load("""
    ancestor(X,Y) <= parent(X,Y)
    ancestor(X,Y) <= parent(X,Z) & ancestor(Z,Y)
""")
# prints a set with one element: the ('bill', 'John Adams') tuple
print(pyDatalog.ask('ancestor(bill, X)')) 



# function
pyDatalog.load("""
    # the manager of bill is John Adams. Bill has only one manager.
    + (manager[bill]=='John Adams') 
""")
# prints a set with one element : the ('bill', 'John Adams') tuple
print(pyDatalog.ask('manager[bill]==X'))



pyDatalog.create_terms('factorial, N')

factorial[N] = N*factorial[N-1]
factorial[1] = 1

print(factorial[3]==N)



# specify how a string can be split, reversibly
pyDatalog.load("""
    split(X, Y,Z) <= (X == Y+'-'+Z)
    split(X, Y,Z) <= (Y == (lambda X: X.split('-')[0])) & (Z == (lambda X: X.split('-')[1]))
""")
# prints a set with one tuple : ('a-b', 'a', 'b')
print(pyDatalog.ask('split("a-b",X,Y)')) 


# aggregate function
pyDatalog.load("""
    (ancestors[X]==concat(Y, key=Y, sep=',')) <= ancestor(X,Y) # the list of ancestors, sorted by their name, and separated by ','
""")
# prints a set with one element: the ('bill', 'John Adams') tuple
print(pyDatalog.ask('ancestors[bill]==X')) 


# formula
pyDatalog.load("""
    Employee.salary_class[X] = Employee.salary[X]//1000    
""")



# unlimited depth of recursion
pyDatalog.load("""
    + even('0')
    even(N) <= (N > 0) & (N1==N-1) & odd(N1)
    odd(N) <= (N > 0) & (N2==N-1) & even(N2)
""")
# prints a set with one element: the ('2000',) tuple
print(pyDatalog.ask('even(2000)')) 

from pyDatalog import pyEngine
pyEngine.Trace = True





