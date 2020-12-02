#!/usr/bin/python3

def valid_password(password):
    # this is the longest fucking instruction i've ever wrote in my life 
    # good luck to whoever's reading this (including futur me)
    return password.split(':')[1].count(password.split(':')[0].split(' ')[1]) in range(int(password.split(':')[0].split(' ')[0].split('-')[0]), int(password.split(':')[0].split(' ')[0].split('-')[1])+1)

puzzle = [ value.rstrip('\n') for value in open('input.txt', 'r').readlines()]
sum = 0

for item in puzzle:
    if(valid_password(item)):
        sum += 1
print(sum)