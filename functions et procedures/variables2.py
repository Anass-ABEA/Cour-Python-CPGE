a = 5
def f():
    global a
    a = 100
    print("la valeur de 'a' à l'intérieur = ",a)

print("la valeur de 'a' avant la fonction = ",a)
f()
print("la valeur de 'a' apres la fonction = ",a)
