file = open("fichier.txt","w") # write - écriture
# si le fichier existe deja le contenu sera écrasé
# si le fichier n'exuiste pas il sera créé

file.write("-chaine de caracteres 1-")
file.write("-chaine de caracteres 2-")

file.close() # fermeture du fichier pour libérer la RAM
