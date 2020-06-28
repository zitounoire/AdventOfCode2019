# RF = RoundDown(M/3) - 3
# Lire Fichier
# Mettre les valeur dans une structure
# Calculer les RF
# Calculer les RF de chaque RF jusqu'a atteindre 0 ou <0
# Additionner et afficher

import math
rf = 0
sum = 0
list = open("input.txt", "r").readlines()
for x in list:
    rf = int(x.rstrip("\n")) 
    while True:
        rf = math.floor(rf / 3) - 2
        if(rf <= 0):
            break
        sum += rf
print(sum)

