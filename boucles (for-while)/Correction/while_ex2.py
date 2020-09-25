# La solution n'est pas unique
# Le jeu aléatoire
import random
############
# méthode 1#
############
aleatoire = random.randint(0,10)
while True:
    entree = int(input("entrer un nombre"))
    if entree == aleatoire:
        print("BINGO")
        break
    else:
        print("faux!!")
############
# méthode 2#
############
aleatoire = random.randint(0,10)
entree = int(input("entrer un nombre"))
while entree!=aleatoire:
    print("faux!!")
    entree = int(input("entrer un nombre"))
#sortie de la boucle donc entree == aleatoire
print("BINGO")
