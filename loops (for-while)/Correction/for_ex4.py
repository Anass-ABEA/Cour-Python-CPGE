# La solution n'est pas unique
import math
############
# méthode 1#
############
for j in range(0,19):
    print("sin(",j*5,") = " ,math.sin(j*5))
############
# méthode 2#
############
for j in range(0,91,5):
    print("sin(",j,") = " ,math.sin(j))
