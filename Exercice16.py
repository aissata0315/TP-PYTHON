#coding : utf-8
dividende = input("donnez la dividende\n:")
dividende = int(dividende)
diviseur = input("donnez le diviseur\n:")
diviseur = int(diviseur)
quotien = 0 
while dividende >= diviseur :
    dividende = dividende - diviseur
    quotien = quotien+1
print(quotien)

