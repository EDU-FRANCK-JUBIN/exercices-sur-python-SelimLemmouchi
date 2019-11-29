# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 20:17:01 2019

@author: Moi
"""

import pandas as pa
from pyDatalog import pyDatalog

# ---------------------------------------------------------------------------
# Social graph analysis:
# work through this code from top to bottom (in the way you would use a R or Jupyter notebook as well...) and write datalog clauses and python code in order to solve the respective tasks. Overall, there are 7 tasks.
# ---------------------------------------------------------------------------
calls = pa.read_csv('calls.csv', sep='\t', encoding='utf-8')
texts = pa.read_csv('texts.csv', sep='\t', encoding='utf-8')

suspect = 'Quandt Katarina'
company_Board = ['Soltau Kristine', 'Eder Eva', 'Michael Jill']

pyDatalog.create_terms('knows', 'has_link', 'many_more_needed', 'X', 'Y', 'Z', 'full_path', 'P', 'P2', 'path_with_cost', 'C', 'C2')
pyDatalog.clear()

# First treat calls simply as social links (denoted knows), which have no date
for i in range(0, 149):
     +knows(calls.iloc[i, 1], calls.iloc[i, 2])



# Task 1: Knowing someone is a bi-directional relationship -> define the predicate accordingly
knows(X, Y) <= knows(Y, X)

#print(knows(suspect, Y))
#print(knows(Y, suspect))

# Task 2: Define the predicate has_link in a way that it is true if there exists some connection (path of people knowing the next link) in the social graph
# Hints:
has_link(X, Y) <= has_link(X, Z) & knows(Z, Y) & (X != Y)
has_link(X, Y) <= knows(X, Y)
#has_link(X, Y) <= has_link(Y, X)


#   check if your predictate works: at least 1 of the following asserts should be true (2 if you read in all 150 communcation records)
#assert (has_link('Quandt Katarina', company_Board[0]))
#assert (has_link('Quandt Katarina', company_Board[1]))
#assert (has_link('Quandt Katarina', company_Board[2]))




# Task 3: You already know that a connection exists; now give the concrete paths between the board members and the suspect
# Hints:
#   if a knows b, there is a path between a and b
#   (X._not_in(P2)) is used to check wether x is not in path P2
#   (P==P2+[Z]) declares P as a new path containing P2 and Z
#full_path(X, Y, P) <= full_path(X, Z, P2) & knows(Z, Y) & (X != Y) & (X._not_in(P2)) & (Y._not_in(P2)) & (P == P2 + [Z])
#full_path(X, Y, P) <= knows(X, Y) & (P == [])
#print(full_path(X, suspect, P))

# Task 4: There are so many path, therefore we are only interested in short pahts.
# find all the paths between the suspect and the company board, which contain five poeple or less
(path_with_cost(X, Y, P, C)) <= (path_with_cost(X, Z, P2, C2)) & knows(Z, Y) & (X != Y) & (X._not_in(P2)) & (Y._not_in(P2)) & (P == P2 + [Z]) & (C == C2 + 1) & (C <= 5)
(path_with_cost(X, Y, P, C)) <= knows(X, Y) & (P == []) & (C == 0)

#print(path_with_cost(suspect, company_Board[2], P, C))

# ---------------------------------------------------------------------------
# Call-Data analysis:
# Now we use the text and the calls data together their corresponding dates
# ---------------------------------------------------------------------------
date_board_decision = '12.2.2017'
date_shares_bought = '23.2.2017'
pyDatalog.create_terms('called,texted', 'valid_dates', 'links', 'links_text', 'links_called', 'links_date', 'D', 'D2', 'P', 'C', 'DC', 'DC2', 'comm', 'P3', 'path_with_cost_d', 'Y', 'X', 'Z', 'P2', 'C2')
pyDatalog.clear()

for i in range(0,149): # calls
    +called(calls.iloc[i,1], calls.iloc[i,2],calls.iloc[i,3])

for i in range(0,149): # texts
    +texted(texts.iloc[i,1], texts.iloc[i,2],texts.iloc[i,3])

called(X,Y,Z) <= called(Y,X,Z) # calls are bi-directional
#texted(X,Y,Z) <= texted(Y,X,Z)


# Task 5: we are are again interested in links, but this time a connection only valid the links are descending in date 
# find out who could have actually sent an information, when imposing this new restriction
# Hints:
#   You are allowed to naively compare the dates lexicographically using ">" and "<"; it works in this example of concrete dates (but is of course evil in general)
#valid_dates(D) <= (D >= date_board_decision) & (D <= date_shares_bought)
#links(X, Y, D) <= ((called(X, Y, D) or texted(X, Y, D)) & valid_dates(D))
#links_text(X, Y, D) <= (texted(X, Y, D) & valid_dates(D))
#links_called(X, Y, D) <= (called(X, Y, D) & valid_dates(D))
#links(X, Y, D) <= (links_called(X, Y, D) or links_text(X, Y, D))


valid_dates(D) <= (D >= date_board_decision) & (D <= date_shares_bought)
links(X,Y,D) <= (called(X,Y,D)) or (texted(X,Y,D))
#print(links(X, Y, D))
links_date(X,Y,D) <= (links(X,Y,D)) & (valid_dates(D))

#Dann werden die pfäde generiert. X ist die Anfangsperson, Y die Endperson. Z ist ein Zwischenmann.
#Es werden verbindungen X->Z->..->Y gespeichert in den path_with_cost_d(X, Z, P2, C2, D2, DC2)) & links_date(Z, Y, D)
#(X != Y) diese Bedingung braucht es, damit keine Loops, mehrere Male über die Selbe Person entstehen
#(X._not_in(P2)) & (Y._not_in(P2)): Ein Kontaktpfad darf nicht mehrere Male über die Anfangs oder Endperson gehen
#deswegen wird geprüft, dass X & Y noch nicht im bestehenden Pfad sind.
#(P == P2 + [Z]): Für die Aufsummierung des Pfades. Der alte Pfad wird mit dem alten + dem neuen Zwischenmann aufsummiert
#(C == C2 + 1): Aufsummierung der Pfadkosten
#(C < 5): Bedingung das Pfade nicht länger als 5 sein dürfen
#(D <= D2): Bedingung das altesdatum älter als neues datum sein muss, sonst ist pfad ungültig
#(DC == DC2 + [D2]): Auflisten der Daten in einem Pfad, aufsumieren alter datumspfad + neues datum
(path_with_cost_d(X, Y, P, C, D, DC)) <= (path_with_cost_d(X, Z, P2, C2, D2, DC2)) & links_date(Z, Y, D) & (X != Y) & (X._not_in(P2)) & (Y._not_in(P2)) & (P == P2 + [Z]) & (C == C2 + 1) & (C < 5) & (D <= D2) & (DC == DC2 + [D2])

#Alle Direkten Links werden zuerst in der PathWithCost liste abespeichert, dies mit leeren Pfaden P und Kostenn überall = 0, das Datum wird übernommen
(path_with_cost_d(X, Y, P, C, D, DC)) <= links_date(X, Y, D) & (P == []) & (C == 0) & (DC == [D])

(comm[X, Y, P3, C, D, DC]==P) <= (path_with_cost_d(X,Y,P,C,D,DC)) & (P3==[X]+P+[Y])


print((comm[suspect,Y,P3,C,D,DC]==P) & (Y.in_(company_Board)))
#print(path_with_cost(suspect, Y, P, C, D, DC))

#print(links_date(suspect, Y, D))
#print('---------------------')
#print(links_called(suspect, Y, D))
#print('---------------------')
#print(links(suspect, Y, D))
# Task 6: at last find all the communication paths which lead to the suspect, again with the restriction that the dates have to be ordered correctly




# Final task: after seeing this information, who, if anybody, do you think has given a tipp to the suspect?




# General hint (only use on last resort!): 
#   if nothing else helped, have a look at https://github.com/pcarbonn/pyDatalog/blob/master/pyDatalog/examples/graph.py