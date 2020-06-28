# upcode:
# 1 => add
# 2 => mult
# 99 => stop
# anything else => something went wrong

# lire position 0 => selectionner op
# lire position +1 => selec op1
# lire position +1 = 2 => selec op2 
# lire position +1 = 3 => selec ret position

i = open("inputd2.txt","r").readline().rstrip("\n").split(',')

pos = 0
tmp = i[pos:pos+4]

while len(tmp) == 4:
    tmp = i[pos:pos+4]
    
    if(tmp[0] == '1'):
        i[int(tmp[3])] = int(i[int(tmp[1])]) + int(i[int(tmp[2])])
    elif(tmp[0] == '2'):
        i[int(tmp[3])] = int(i[int(tmp[1])]) * int(i[int(tmp[2])])
    elif(tmp[0] == '99'):
        print(",".join(str(v) for v in i))
        break
    else:
        print("something went wrong\n")
        print(",".join(str(v) for v in i))
        break
    pos += 4