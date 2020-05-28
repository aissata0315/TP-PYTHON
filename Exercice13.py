# coding: utf-8
jour = input("donnez le jour")
jour = int(jour)
mois = input("donnez le mois")
mois = int(mois)
annee = input("donnez l'annee")
annee = int(annee)
liste1 = {"01","03","05","07","08","10","12"}
for i in liste1 : 
    if jour <=31 : 
        print("date valide")
    else:
        print("date invalide")
liste2 = {"04,06,09,11"}
for i in liste2 : 
    if jour <=30 :
        print("date valide")
    else:
        print("date invalide")
if mois == "02" and jour<=29 :
    print("date valide")

