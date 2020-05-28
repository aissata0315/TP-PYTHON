# coding: utf-8
tableau = []
croissant = True
decroissant = True
i = 0
while i < 10 :
    nombre = input("donnez un entier:\n")
    tableau.append(nombre)
    i = i+1

i = 0
while i < len(tableau)-1 :
    if tableau[i] < tableau[i+1] :
        decroissant = False
    if tableau[i] > tableau[i+1] :
        croissant = False
    i = i+1

if croissant == True:
    print('ordre croissant')
if decroissant == True:
    print("ordre decroissant")

