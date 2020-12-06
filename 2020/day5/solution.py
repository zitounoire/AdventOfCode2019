#!/usr/bin/python3

billets = [item.strip() for item in open('input.txt','r').readlines()]

IDs_list = [int(billet.replace('F','0').replace('B','1').replace('L','0').replace('R','1'),2) for billet in billets]

test =[15,944,945,946,947]
for row in range(2,118):
    for col in range(8):
        test.append(row*8+col)

print('Part 1:', max(IDs_list))
print('Part 2:',set(test).symmetric_difference(set(IDs_list)))
