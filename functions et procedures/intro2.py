import datetime
import sys

# Defition des fonctions et procédures.
def afficher_personne(nom):
    print("Bonjour Mlle/Mr "+nom)
def afficher_menu():
    print("---------------------------")
    print("---- affichage du menu ----")
    print("---------------------------")
    print("-1- afficher la date      -")
    print("-2- afficher l'heure      -")
    print("-0- quitter le programme  -")
    print("---------------------------")
def afficher_resultat(entree):
    now = datetime.datetime.now()
    if entree== 1:
        print (now.strftime("%Y-%m-%d %Hsc:%M:%S"))
    elif entree= 2:
        print (now.strftime("%Hsc:%M:%S"))
    else:
        # rien à faire donc l'exercution s'arrete
        pass

# Execution
nom = input("entrez votre nom")
afficher_personne(nom)
afficher_menu()
entree = int(input("choix (0/1/2): "))
afficher_resultat(entree)
