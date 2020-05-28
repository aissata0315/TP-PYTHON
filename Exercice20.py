#coding : utf-8
tableau = []
i = 0
max = 0
indice = 0
while i < 10 :
    nombre = input("donnez un entier")
    nombre = int(nombre)
    tableau.append(nombre)
    i = i+1
    if nombre > max : 
        max = nombre
        indice = 1
print(max,indice)