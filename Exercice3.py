# coding: utf-8

R1 = input("Entrez la resistence r1\n")
R1 = float(R1)
R2 = input("Entrez la resistence r2\n")
R2 = float(R2)
R3 = input("Entrez la resitence r3\n")
R3 = float(R3)
RS = R1+R2+R3
print("la resistence en serie:",RS)
if R1==0 and R2==0 | R2==0 and R3==0 | R1==0 and R3==0 : 
   
    print("Impossible de calculer la resistence en parallele")
else:
    RP = (R1*R2*R3) / (R1*R2+R1*R3+R2*R3)
    print("la resistence en parallele est:", RP)