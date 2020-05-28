# coding: utf-8

def echange(x,y):

    if x>y:
        z = x
        x = y
        y = z
    return(x,y)

A = input("donnez l'entier a\n")
A = int(A)
B = input("donnez l'entier b\n")
B = int(B)
C = input("donnez l'entier b\n")
C = int(C)
A,B = echange(A,B)
A,C = echange(A,C)
B,C = echange(B,C)
print(A,B,C)

