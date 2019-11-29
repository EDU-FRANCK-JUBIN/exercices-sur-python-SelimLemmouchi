# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 19:31:06 2019

@author: Moi
"""

from sqlalchemy.ext.declarative import declarative_base; from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker; from pyDatalog import pyDatalog
# define a base class with SQLAlchemy and pyDatalog capabilities
Base = declarative_base(cls=pyDatalog.Mixin, metaclass=pyDatalog.sqlMetaMixin)
# load a database from the same directory and create a session, then associate it to the Base class

engine = create_engine('sqlite:///chinook.db') #, echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base.session = session

# classes that inherit from Base will now have both pyDatalog and SQLAlchemy capability
# the approach can be used to load an existing KB from a database relation, using __table_args__ :
class Track(Base):
    __tablename__ = 'tracks'
    __table_args__ = {'autoload':True, 'autoload_with':engine} #autoload the model
    def __repr__(self): #specifies how to print a Track
        return "'" + self.Name + "' costs $" + str(self.UnitPrice)
# the Track class can now be used in in-line queries; example: which track is at least 5s long?

X = pyDatalog.Variable()
Track.Milliseconds[X] >= 5000000
print(X) #outputs ['Through a Looking Glass' costs $1.99, 'Occupation / Precipice' costs $1.99]


