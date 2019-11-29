print("Pour l'exercice, il faut installer numpy dans votre environnement")

import numpy as np
print(np.__version__)

# import math

e = np.exp(1)
# print("e = ", e)

# n = int(input('Entrer un numéro plus grand que 50: '))

 
def exponential(n, x): 
  
    sum = 1.0 
    for i in range(n, 0, -1): 
        sum = 1 + x * sum / i 
    print ("e^x =", sum) 

#n = 10
n = int(input('Entrer un numéro plus grand que 50: '))
x = 1.0
exponential(n, x) 

# print("L'erreur est de ", e - exponential(n, x))
