# La solution n'est pas unique
############
# méthode 1#
############
L = [1,3,4,8,9,11,15]
for i in L:
    for j in range(1,11):
        print(i,"x",j,"=",i*j)
    print("")
############
# méthode 2#
############
L = [1,3,4,8,9,11,15]
for i in L:
    for j in range(i,(10*i)+1,i):
        print(j)
    print("")
