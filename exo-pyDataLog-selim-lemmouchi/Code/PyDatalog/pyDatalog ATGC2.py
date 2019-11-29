# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 20:19:09 2019

@author: Moi
"""

import random
import time

from pyDatalog import pyDatalog

alphabet = ['A','T','G','C','N']

# string length function
def strlen(x):
    if isinstance(x,basestring):
        return len(x)
    return 0

# character equality function
# this is a python function, so in true pythonic fashion, the comparison is very general
# here, we just mean to use it as character comparison
def match(a,b):
    return a==b

pyDatalog.create_terms('strlen, match')

def rand_string_n(n):
    """
    Returns a random string of A,T,G,C characters of length n.
    """
    return ''.join([random.choice(['A','T','G','C']) for i in range(n)])


# implementing tries in datalog as FSMs

pyDatalog.create_terms('trie_root,trie_edge,trie_final,N,N1,N2')

# trie_edge(a,b,c): there is an edge from node a to node b labeled with
# character c.

+trie_root(0)
+trie_edge(-1,-2,'')
root_node = 0
# because python is weird
max_node = {0:0}

def add_string_to_trie(s):
    """
    Adds a string to the trie
    TODO: is there a way to do this only using datalog?
    """
    n1 = root_node
    for c in s:
        if not trie_edge(n1, N, c):
            +trie_edge(n1,max_node[0]+1,c)
            max_node[0]+=1
        n1 = trie_edge(n1, N, c)[0][0]
    +trie_final(n1)


pyDatalog.create_terms('trie_query,X,X1,S')

trie_query(X,'') <= trie_final(X)
trie_query(X,S) <= (trie_edge(X,X1,S[0]) & trie_query(X1,S[1:]))

if __name__ == '__main__':
    t = time.time()
    strings = []
    for i in range(100):
        s = rand_string_n(20)
        add_string_to_trie(s)
        strings.append(s)
    print('Time elapsed for trie construction: {0}'.format(time.time()-t))
    t = time.time()
    results = (X.in_(strings) & trie_query(root_node,X))
    assert(len(results)==100)
    print('Time elapsed for trie querying: {0}'.format(time.time()-t))