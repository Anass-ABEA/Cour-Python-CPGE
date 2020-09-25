import datetime
import sys

now = datetime.datetime.now()
n = input("entrez votre nom")
print("Bonjour Mlle/Mr "+n)
print("---------------------------")
print("---- affichage du menu ----")
print("---------------------------")
print("-1- afficher la date      -")
print("-2- afficher l'heure      -")
print("-0- quitter le programme  -")
print("---------------------------")
entree = int(input("choix (0/1/2): "))

if entree== 1:
    print (now.strftime("%Y-%m-%d %Hsc:%M:%S"))
elif entree= 2:
    print (now.strftime("%Hsc:%M:%S"))
else:
    # rien à faire donc l'exercution s'arrete
    pass
