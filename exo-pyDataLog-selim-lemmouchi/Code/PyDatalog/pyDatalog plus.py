# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 17:02:20 2019

@author: Moi
"""

from pyDatalog import pyDatalog
pyDatalog.create_terms('X,Y,manager, count_of_direct_reports')

# the manager of Mary is John
+(manager['Mary'] == 'John')
+(manager['Sam']  == 'Mary')
+(manager['Tom']  == 'Mary')

(count_of_direct_reports[X]==len_(Y)) <= (manager[Y]==X)
print(count_of_direct_reports['Mary']==Z)



from pyDatalog import pyDatalog
pyDatalog.create_terms('X,Y,Z, works_in, department_size, manager, indirect_manager, count_of_indirect_reports')

# Mary works in Production
+ works_in('Mary', 'Production')
+ works_in('Sam',  'Marketing')

+ works_in('John', 'Production')
+ works_in('John', 'Marketing')

_works_in = set()
_works_in.add(('Mary', 'Production'))
_works_in.add(('Sam',  'Marketing'))
_works_in.add(('John', 'Production'))
_works_in.add(('John', 'Marketing'))

# give me all the X that work in Marketing
print(works_in(X,  'Marketing'))
print

# procedural equivalent in Python
for i in _works_in:
    if i[1]=='Marketing':
        print i[0]


# one of the indirect manager of X is Y, if the (direct) manager of X is Y
indirect_manager(X,Y) <= (manager[X] == Y)
# another indirect manager of X is Y, if there is a Z so that the manager of X is Z, 
#   and an indirect manager of Z is Y
indirect_manager(X,Y) <= (manager[X] == Z) & indirect_manager(Z,Y)
print(indirect_manager('Sam',X))


# the manager of John is Mary (whose manager is John !)
manager['John'] = 'Mary'
print(indirect_manager('John',X))


# John does not work in Production anymore
- works_in('John', 'Production')

(count_of_indirect_reports[X]==len_(Y)) <= indirect_manager(Y,X)
print(count_of_indirect_reports['John']==Y)



pyDatalog.create_terms('factorial, N')

factorial[N] = N*factorial[N-1]
factorial[1] = 1

print(factorial[3]==N)



pyDatalog.create_terms('link, can_reach')

# there is a link between node 1 and node 2
+link(1,2)
+link(2,3)
+link(2,4)
+link(2,5)
+link(5,6)
+link(6,7)
+link(7,2)


# links are bi-directional
link(X,Y) <= link(Y,X)



# can Y be reached from X ?
can_reach(X,Y) <= link(X,Y) # direct link
# via Z
can_reach(X,Y) <= link(X,Z) & can_reach(Z,Y) & (X!=Y)

print (can_reach(1,Y))


