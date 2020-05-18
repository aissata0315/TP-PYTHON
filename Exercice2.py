 # coding: utf-8


import math as m

rayon = input("donnez le rayon\n")
rayon = float(rayon)

perimetre = 8*rayon*m.atan(1)
surface = 4*rayon*rayon*m.atan(1)

texte= "Le perimetre du cercle de rayon {} est {} et sa surface est{}"
print(texte.format(rayon,perimetre,surface))