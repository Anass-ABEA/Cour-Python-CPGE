file = open("fichier.txt","a") # append - ajout
# si le fichier existe deja le contenu sera écrasé
# si le fichier n'exuiste pas il sera créé

file.write("-chaine de caracteres 3-\n")
file.write("-chaine de caracteres 4-\n")

file.close() # fermeture du fichier pour libérer la RAM
