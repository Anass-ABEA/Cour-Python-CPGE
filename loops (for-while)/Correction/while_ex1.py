# La solution n'est pas unique
############
# méthode 1#
############
while True:
    var = int(input("entrer un nombre"))
    if var >= 100 :
        print("OVER")
        break
    if var <= 20:
        print("UNDER")
        break

############
# méthode 2#
############
var = int(input("entrer un nombre"))
while (20<var<100):
    var = int(input("entrer un nombre"))
# sortie de la boucle donc soit var <20 soit var >100
if var >= 100 :
    print("OVER")
else:
    print("UNDER")
