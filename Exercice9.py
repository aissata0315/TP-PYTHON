#coding : utf-8
import math as m

heuredep = input("heure de depart")
heuredep = int(heuredep)

minutedep = input("minute de depart")
minutedep = int(minutedep)

hdar = input("heure d'arrive")
hdar = int(hdar)

minutedar = input("minute d'arrivee")
minutedar = int(minutedar)

Hdep_mn = heuredep*60 + minutedep
Hdar_mn = hdar*60 + minutedar

duree_en_mn = (Hdar_mn - Hdep_mn)
heure_dure = m.floor(duree_en_mn/60)
minute_duree = duree_en_mn%60

print(heure_dure,minute_duree)