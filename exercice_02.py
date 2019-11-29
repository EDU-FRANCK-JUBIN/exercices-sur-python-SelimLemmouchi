print("Programme permettant de donner tous les diviseurs communs d'un nombre entier supérieur à 1 et dire sinon dire qu'il est premier")

import math

n = int(input('Entrer le nombre: '))

for i in range(1, n+1) :
    if(n%i==0):
        print(i)
    elif (n%i !=0) :
        print("%.0f est un nombre premier" %n)


# If given number is greater than 1 
# if n > 1: 
      
#    # Iterate from 2 to n / 2  
#    for i in range(2, n//2): 

#        if (n % i) == 0: 
#            print(n, "n'est pas un nombre premier")
#            print(i) 
           
#    else: 
#        print(n, "est un nombre premier") 
  
# else: 
#    print(n, "is not a prime number") 

# Amélioration 1 : Dire le nombres de diviseurs sans compter 1 et n