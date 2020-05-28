# coding : utf-8
nombresecret = input("Donnez un nombre secret\n")
nombresecret = int(nombresecret)
i = 0
while i != nombresecret : 
    i = int(input("devinez le nombre"))
    if i > nombresecret : 
        print("trop grand")
    if i < nombresecret : 
        print("trop petit")
    if nombresecret == i :
        print ("bravo")

