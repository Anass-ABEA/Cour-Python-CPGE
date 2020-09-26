file = open("file.txt","r") # read - lecture
# si le fichier existe deja le contenu sera écrasé
# si le fichier n'exuiste pas on auras une erreur

text = file.read()
print(text)

file.close() # fermeture du fichier pour libérer la RAM
