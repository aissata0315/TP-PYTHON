#coding : utf-8
def pgcd(a,b) :  
   while a%b != 0 : 
      a, b = b, a%b 
   return b
entier1 = input("donnez l'entier 1:")
entier1 = int(entier1)
entier2 = input("donnez l'entier 2")
entier2 = int (entier2)
print "le pgcd de", entier1, "et", entier2, "est", pgcd(entier1,entier2)