def liste_trie(liste):
    for i in range(1,len(liste)):
        if liste[i]< liste[i-1]:
            return False
    return True
