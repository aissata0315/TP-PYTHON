# coding: utf-8

import math as m

a = input("donnez la valeur de a\n")
b = input("donnez la valeur de b\n")
a= int(a)
b= int(b)
if b==0 :
    print("impossible de faire la division")
else :
    quotient = m.floor(a/b)
    reste = a%b
    ratio = 100*a/b

texte = ("le quotient de la division de a par b est {}, le reste est {} et le ratio {}")

print(texte.format(quotient,reste,ratio))













