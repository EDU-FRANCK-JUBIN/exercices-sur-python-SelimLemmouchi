# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:39:10 2019

@author: Moi
"""

from pyDatalog import pyDatalog

class Employee(object):
    
    def __init__(self, name, manager, salary): # method to initialize Employee instances
        super(Employee, self).__init__() # calls the initialization method of the object class
        self.name = name
        self.manager = manager           # direct manager of the employee, or None
        self.salary = salary             # monthly salary of the employee
    
    def __repr__(self): # specifies how to display an Employee
        return self.name

John = Employee('John', None, 6800)
Mary = Employee('Mary', John, 6300)

pyDatalog.assert_fact('has_car', Mary)
print(pyDatalog.ask('has_car(X)')) # prints a set with one element : the (Mary) tuple




from pyDatalog import pyDatalog 

class Employee(pyDatalog.Mixin): # --> Employee inherits the pyDatalog capability
    
    def __init__(self, name, manager, salary): 
        # call the initialization method of the Mixin class
        super(Employee, self).__init__()
        self.name = name
        self.manager = manager     # direct manager of the employee, or None
        self.salary = salary       # monthly salary of the employee
    
    def __repr__(self): # specifies how to display an Employee
        return self.name

John = Employee('John', None, 6800)
Mary = Employee('Mary', John, 6300)
Sam = Employee('Sam', Mary, 5900)

print(pyDatalog.ask('Employee.salary[X]==6300')) # prints a set with 1 element : the (Mary, 6300) tuple



pyDatalog.create_terms('has_car, X')
+ has_car(Mary)
print(has_car(X)) # prints a list with one answer: the (Mary,) tuple


# all the indirect managers Y of X are derived from his manager, recursively
Employee.indirect_manager(X,Y) <= (Employee.manager[X]==Y) & (Y != None)
Employee.indirect_manager(X,Y) <= (Employee.manager[X]==Z) & Employee.indirect_manager(Z,Y) & (Y != None)

# the salary class N of employee X is a function of his/her salary
# this statement is a logic equality, not an assignment !
Employee.salary_class[X] = Employee.salary[X]//1000

# What is the salary class of John ?
print(John.salary_class) # prints 6



# calculated attribute
Mary.salary_class = ((Employee.salary_class[Mary]==X) >= X) 




# Who are the employees of John with a salary class of 5 ?
result = (Employee.salary_class[X] == 5) & Employee.indirect_manager(X, John)
print(result) # prints [(Sam,)]



E = Employee # defines an alias for Employee
Employee.salary_class[X] = E.salary[X]//1000



class Employee(pyDatalog.Mixin):   # inherits pyDatalog capability
    <same definition of Employee as above>

    @pyDatalog.program() # the following function contains pyDatalog clauses
    def _():
        Employee.salary_class[X] = E.salary[X]//1000
        
        
        
        

