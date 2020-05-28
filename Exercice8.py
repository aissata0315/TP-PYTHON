# coding: utf-8
import math as m
a = input("donnez la valeur de a: ")
a = int(a)
b = input("donnez la valeur de b: ")
b = int(b)
c = input("donnez la valeur de c: ")
c = int(c)

Delta = (b*b)-(4*a*c)


if Delta>0 : 
    x1 = int((-b -m.sqrt(Delta)) / (2*a))
    x2 = int((-b +m.sqrt(Delta)) / (2*a))
    print("sont les solutions", x1,x2) 


if Delta == 0 :
    x0 = -b / 2*a
    print("est la solution",x0)

if Delta < 0 :
    print("impossible")
