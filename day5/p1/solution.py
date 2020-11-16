# since i'm using the same code from day2 and it will probably be required to change again during future days.
# I decided to refactor the code to make it more managable in the future.
# That's what's cool with code you can do whatever the fuck you want to do and no one can judge you because no one understand what the fuck you've done.

# opcode:
# 1 => add
# 2 => mult
# 99 => stop
# anything else => something went wrong

# TO DO:
# ------
# 3 => takes an input and puts in the adresse given by its only operator (Ex: 3,50)
# 4 => output operation, does the same thing as 3 but it's output inseat of input.

# the types of programs provided for this compiler come with instruction that say what the input should be

# MODES:
# ------
# the compiler also adds the notion of position and immidiate mode.
#
#  - Position mode: params are interpreted as adresses or positions
#  - Immidiate mode: params are interpreted as values
#
# params modes are stored in the same value as the instruction's opcode. The are single digits and read right to left

# -------------------------------------------------------------------------------------------------------
# ABCDE
#  1002

# DE - two-digit opcode,      02 == opcode 2
#  C - mode of 1st parameter,  0 == position mode
#  B - mode of 2nd parameter,  1 == immediate mode
#  A - mode of 3rd parameter,  0 == position mode, (omitted due to being a leading zero)
# -------------------------------------------------------------------------------------------------------

# Parameters that an instruction writes to will never be in immediate mode. (ie: op3 for for 3 argument instructions and op for read write instructions)

# Important:
# ----------
# the IP (instruciton pointer) should increase by the number of values in the instruction. 4 or 2 depending on the instruction
# Integers can be negative in the input



# extract params modes and op code
# works but needs optimazation probably should use list comprehensions(?)
# basically converts an int to a list 
# is there already a functions in the standard library that does this ?
# too stoned to care

def opcode_interpreter(opcode):

    mod1 = opcode // 10000
    opcode %= 10000
    mod2 = opcode // 1000
    opcode %= 1000
    mod3 = opcode // 100
    opcode %= 100
    op = opcode % 10
    # print([mod1, mod2, mod3, op])
    return [mod1, mod2, mod3, op]


# handles read/write ops
def read_write(memory, opcode, instruction):
    #print(instruction)
    if(opcode[-1] == 3):
        memory[instruction[1]] = int(input()) # read
    else:
        if opcode[2] == 0:
            print(memory[instruction[1]])
        else:
            print(instruction[1])


#   This function takes an instruction and interprets it then returns the length of the next step in the program
# Input: instruction. A list with len(list) == 4 (i'll deal with the step size internally)
# Output: int. size of step in the program
# remember to put a ternary operation to 
#  a = 2 + 3 if (1==0) else 2*3

def intcode_interpreter(memory, instruction):
    step = 4

    opcode_list = opcode_interpreter(int(instruction[0]))

    # it really sucks that python doesn't implement a switch case
    # print(opcode_list)
    if (opcode_list[-1] == 3 or opcode_list[-1] == 4):
        read_write(memory, opcode_list, instruction)
        step = 2
    else:
        if (not(opcode_list[1]) and not(opcode_list[2])): 
            # both are in position mode
            memory[instruction[-1]] = memory[instruction[1]] + memory[instruction[2]] if (opcode_list[-1] == 1) else memory[instruction[1]] * memory[instruction[2]]
        elif (opcode_list[1] and not(opcode_list[2])):
            # first is in position mode second in immidiate
            memory[instruction[-1]] = memory[instruction[1]] + instruction[2] if (opcode_list[-1] == 1) else memory[instruction[1]] * instruction[2]
        elif (not(opcode_list[1]) and opcode_list[2]):
            # first is in immidiate mode second in position
            memory[instruction[-1]] = instruction[1] + memory[instruction[2]] if (opcode_list[-1] == 1) else instruction[1] * memory[instruction[2]]
        elif (opcode_list[1] and opcode_list[2]):
            # both are in immidiate mode
            memory[instruction[-1]] = instruction[1] + instruction[2] if (opcode_list[-1] == 1) else instruction[1] * instruction[2]
        else:
            print('[!] Something went wrong!')
    return step

i = open("input.txt","r").readline().rstrip("\n").split(',')
i = [int(el) for el in i]
#print(i)

pos = 0
inst = i[pos:pos+4]

while len(inst) == 4:
    inst = i[pos:pos+4]
    #print(inst)
    if (inst[0] == 99):
        break
    pos += intcode_interpreter(i, inst)