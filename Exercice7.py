# coding: utf-8
import math as m
montant = input("Donnez le montant à convertir: ")
montant = int(montant)
B20 = m.floor(montant/20)
x = montant%20
B10 = m.floor(x/10)
y = x%10
B5 = m.floor(y/5)
z = y%5
P2 = m.floor(z/2)
t = z%2
P1 = t
print(B20,B10,B5,P2,P1)