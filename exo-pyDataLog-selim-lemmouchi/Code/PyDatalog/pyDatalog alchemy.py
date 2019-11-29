# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 17:41:07 2019

@author: Moi
"""

from sqlalchemy.ext.declarative import declarative_base

# define a base class with SQLAlchemy and pyDatalog capabilities
Base = declarative_base(cls=pyDatalog.Mixin, metaclass=pyDatalog.sqlMetaMixin)




from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# create database in memory
engine = create_engine('sqlite:///:memory:', echo=False)

# open a session on a database, then associate it to the Base class
Session = sessionmaker(bind=engine)
session = Session()
Base.session = session



from sqlalchemy import Column, Integer, String, ForeignKey

class Employee(Base): # Employee inherits from the Base class
    __tablename__ = 'employee' # data are stored in the Employee table

    name = Column(String, primary_key=True)
    manager_name = Column(String, ForeignKey('employee.name'))
    salary = Column(Integer)

# now create the table
Base.metadata.create_all(engine)



class Employee(Base):
    __tablename__ = 'employee'
    __table_args__ = {'autoload':True} # autoload the model
    
    
    
# who has a salary of 6300 ?
X = pyDatalog.Variable()
Employee.salary[X] == 6300
print(X) # prints [Employee: Mary]

X[0].salary = 3000 # modify in-session data
Employee.salary[X] == 3000
print(X)  # prints [Employee: Mary]



from pymongo import Connection
connection = Connection()
db = connection.Employees
profiles = db.profiles

profiles_to_insert = [{"name": "John", "diploma": "MSc."},
                     {"name": "Mary", "diploma": "EE"},
                     {"name": "Sam", "diploma": "MBA"}]

profiles.insert(profiles_to_insert)




from SQLAlchemy import Employee # import the SQLAlchemy example

def _pyD_diploma2(cls, employee, diploma):
    global profiles
    if employee.is_const():
        r = profiles.find_one({"name": employee.id.name})
        if r: yield (employee, r["diploma"])
        return
    raise AttributeError

# attach the resolver to the Employee class
Employee._pyD_diploma2 = classmethod(_pyD_diploma2) 




from pyDatalog import pyDatalog
X, N, Diploma = pyDatalog.variables(3)

# Who has a salary of 6800 and a MSc. diploma
(Employee.salary[X]==6800) & (Employee.diploma[X]=="MSc.")
print(X) # prints [Employee: John]





