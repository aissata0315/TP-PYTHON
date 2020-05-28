# coding: utf-8
jour = input("donnez le jour")
jour = int(jour)
mois = input("donnez le mois")
mois = int(mois)
annee = input("donnez l'annee")
annee = int(annee)
if mois == 1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10 or mois == 11 :
    if jour <=31 : 
        print("date valide")
    else :
        print("date invalide")
if mois == 4 or mois == 6 or mois == 9 or mois == 11 :
    if jour <=30 :
        print("date valide")
    else:
        print("date invalide")
if mois == 2 and jour<=29 :
    print("date valide")
else:
    print("date invalide")

