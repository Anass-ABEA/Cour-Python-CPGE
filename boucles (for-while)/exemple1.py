L = range(9,15)
i = 0
while i < len(L):
    if L[i]%2 == 0:
        print("element est pair")
    else:
        print("element est impair")
    print("indice i= "+str(i)+" element = "+str(L[i]))
    i+=1
