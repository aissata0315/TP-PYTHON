# coding: utf-8

def Comparaison(x,y):

    if x>y:
        z = x
        x = y
        y = z

A = input("donnez l'entier a\n")
A = int(A)
B = input("donnez l'entier b\n")
B = int(B)
C = input("donnez l'entier c\n")
C = int(C)
Comparaison(A,B)
Comparaison(B,C)
Comparaison(A,C)
print(A,B,C)

