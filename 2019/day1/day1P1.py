# RF = RoundDown(M/3) - 3
# Lire Fichier
# Mettre les valeur dans une structure
# Calculer les RF
# Additionner et afficher

import math
sum = 0
list = open("input.txt", "r").readlines()
for x in list:
    sum += math.floor(int(x.rstrip("\n")) / 3) - 2 
print(sum)

