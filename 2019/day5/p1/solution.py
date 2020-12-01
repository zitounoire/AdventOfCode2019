# upcode:
# 1 => add
# 2 => mult
# 99 => stop
# anything else => something went wrong

# lire position 0 => selectionner op
# lire position +1 => selec op1
# lire position +1 = 2 => selec op2 
# lire position +1 = 3 => selec ret position
# Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. For example, the instruction 3,50 would take an input value and store it at address 50.
# Opcode 4 outputs the value of its only parameter. For example, the instruction 4,50 would output the value at address 50.

i = open("input.txt","r").readline().rstrip("\n").split(',')

pos = 0
tmp = i[pos:pos+4]
print(len(i))

while len(tmp) == 4:
    tmp = i[pos:pos+4]
    #print(tmp)
    Opcode = tmp[0]
    if int(tmp[0][-1]) != 4 :
        op1 = i[int(tmp[1])]
        op2 = i[int(tmp[2])]
        
    if len(str(Opcode)) > 1 :
        if len(str(Opcode)) == 3:
            Opcode = '0' + str(Opcode)
        if str(Opcode)[0:2] == '11':
            op1 = tmp[1]
            op2 = tmp[2]
        elif str(Opcode)[0:2] == '01':
            op1 = tmp[1]
        elif str(Opcode)[0:2] == '10':
            op2 = tmp[2]
            #print("Opcode error == ", pos, tmp)
            #break
        Opcode = str(Opcode)[-1]
    print(Opcode)
    #print(pos)
    if(Opcode == '1'):
        i[int(tmp[3])] = str(int(op1) + int(op2))
    elif(Opcode == '2'):
        i[int(tmp[3])] = str(int(op1) * int(op2))
    elif(Opcode == '3'):
        i[int(tmp[1])] = input()
        pos += 2
        continue
    elif(Opcode == '4'):
        print(i[int(tmp[1])])
        pos += 2
        continue
    elif(tmp[0] == '99'):
        print(",".join(str(v) for v in i))
        break
    else:
        print("something went wrong\n")
        print(",".join(str(v) for v in i))
        break
    pos += 4