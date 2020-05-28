nombre = input("Entrez un entier:\n")
nombre = int(nombre)
i=1
somme =0
while i <= nombre/2 :
    if (nombre%i) == 0:
        somme=somme+i
        i = i+1
if nombre == somme :
    print("le nombre saisi et un nombre parfait")
else:
    print("le nombre saisi n'est pas parfait")


