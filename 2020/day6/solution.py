#!/usr/bin/python3

puzzle = [len(set(item)) for item in ''.join(open('input.txt','r').readlines()).replace('\n', '-').replace('--', '\n').replace('-',' ').strip(' ').replace(' ', '').split('\n')]
print(sum(puzzle))

puzzle2 = [item.split(',') for item in ''.join(open('input.txt','r').readlines()).replace('\n', '-').replace('--', '\n').replace('-',' ').strip(' ').replace(' ', ',').split('\n')]
sum = 0
for item in puzzle2:
    sum +=len(set.intersection(*[set(x) for x in item]))
print(sum)

