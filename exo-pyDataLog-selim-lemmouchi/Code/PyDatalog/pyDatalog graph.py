# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 18:12:53 2019

@author: Moi
"""

print("all path from/to 1")
	all_path(X,Y,P) <= all_path(X,Z,P2) & link(Z,Y) & (X!=Y) & (X._not_in(P2)) & (Y._not_in(P2)) & (P==P2+[Z])
	all_path(X,Y,P) <= link(X,Y) & (P==[])

	print (all_path(X,1,P))
    
    