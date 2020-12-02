#!/usr/bin/python3

# It took me for ever to figure out that it was a xor instead of an or i feel like shit

def valid_password(password):
    # didn'y adjust the indexes because i don't clear password of the leading space charachter
    return bool(password.split(':')[1][int(password.split(':')[0].split(' ')[0].split('-')[0])] == password.split(':')[0].split(' ')[1]) ^ bool(password.split(':')[1][int(password.split(':')[0].split(' ')[0].split('-')[1])] == password.split(':')[0].split(' ')[1])

puzzle = [ value.rstrip('\n') for value in open('../p1/input.txt', 'r').readlines()]
sum = 0

for item in puzzle:
    if(valid_password(item)):
        sum += 1
print(sum)

