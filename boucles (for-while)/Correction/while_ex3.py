# La solution n'est pas unique
############
# méthode 1#
############
somme = 0
nbr = 0
while True:
    var = int(input("entrer un nombre"))
    if var >0 :
        somme = somme + var
        nbr +=1
    else:
        print("somme",somme")
        print("moyenne",somme/nbr)
        break


############
# méthode 2#
############
somme = 0
nbr = 0
var = int(input("entrer un nombre"))
while var > 0:
    somme = somme + var
    nbr +=1
    var = int(input("entrer un nombre"))
# hors de la bouce donc var <=0
print("somme",somme")
print("moyenne",somme/nbr)
