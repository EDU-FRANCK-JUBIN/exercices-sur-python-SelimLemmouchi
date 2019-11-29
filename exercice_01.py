print("Calcul du volume d'un cône droit")

import math

r = float(input('Entrer le rayon du cône: '))
h = float(input('Entrer la hauteur du cône : '))

print("La formule mathématique pour calculer le volume d'un cône droit est : pi x R^2 x h / 3")

v = (1.0/3) * math.pi * r * r * h

print(" Le volume du cône est de %.2f" %v);