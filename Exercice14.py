#coding : utf-8
jour = input("donnez le jour")
jour = int(jour)
mois = input("donnez le mois")
mois = int(mois)
annee = input("donnez l'annee")
annee = int(annee)

if annee%4==0 and annee%100!=0 or annee%400==0 :
    print("anne bissextille")
else:
    print("anne non bissextille")

