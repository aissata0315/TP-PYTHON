# coding : utf-8
tableau = []
longueur = 0
i = 0
longueur_du_tableau = int (input("donnez la taille du tableau:\n"))
while i < longueur_du_tableau :
	nombre = int (input("donnez un entier:\n"))
	if nombre <  100 : 
		tableau.append(nombre)
		i = i+1
while i < len(tableau) - 1 : 
	k = i
	j = i+1
	while tableau[k]< tableau[j] :
		k = k+1
		j = j+1
	if j-i > longueur :
		debut = i
		fin = k
		longueur = j-i
	i = k
	print(longueur)







