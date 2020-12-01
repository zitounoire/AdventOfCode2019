
z = open("puzzle.txt","r").readline().rstrip("\n").split(',')
z = [int(g) for g in z]

i = z.copy()
couples = []

for c1 in range(100):
    for c2 in range(100):
        i[1] = c1
        i[2] = c2

        pos = 0
        tmp = i[pos:pos+4]

        while len(tmp) == 4:

            tmp = i[pos:pos+4]

            if(tmp[0] == 1):
                i[tmp[3]] = i[tmp[1]] + i[tmp[2]]
            elif(tmp[0] == 2):
                i[tmp[3]] = i[tmp[1]] * i[tmp[2]]
            elif(tmp[0] == 99):
                if i[0] == 19690720:
                    print("noune = " , c1, "\nverbe = ",c2)
                i = z.copy()
                break
            else:
                print("something went wrong\n", i[0],"\n")
                break
            pos += 4