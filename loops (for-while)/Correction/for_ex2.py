# La solution n'est pas unique
############
# méthode 1#
############
for i in range(1,11):
    for j in range(1,11):
        print(i,"x",j,"=",i*j)
    print("")
############
# méthode 2#
############
for i in range(1,11):
    for j in range(i,(10*i)+1,i):
        print(j)
    print("")
