#!/usr/bin/python3
import re
# the following generates a list of dictionaries
documents = [dict(e.split(':') for e in item.split(',')) for item in ''.join(open('input.txt','r').readlines()).replace('\n', '-').replace('--', '\n').replace('-',' ').strip(' ').replace(' ', ',').split('\n')]

required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

def check_validity(document):
    if not(1920 <= int(document['byr']) <= 2002):
        return False
    if not(2010 <= int(document['iyr']) <= 2020):
        return False
    if not(2020 <= int(document['eyr']) <= 2030):
        return False
    r1 = re.compile('^[0-9]{3}cm$|^[0-9]{2}in$')
    if not(r1.match(document['hgt'])):
        return False
    if (document['hgt'][3:] == 'cm' and not(150 <= int(document['hgt'][:3]) <= 193)) or (document['hgt'][3:] == 'in' and not(59 <= int(document['hgt'][:3]) <= 76)):
        return False
    regex = re.compile('^[#][0-9a-f]{6}$')
    if not(regex.match(document['hcl'])):
        return False
    if (document['ecl'] not in ['amb','blu','brn','gry','grn','hzl','oth']):
        return False
    regex1 = re.compile('^[0-9]{9}$')
    if not(regex1.match(document['pid'])):
        return False
    return True

# Part 1
sum = 0
for document in documents:
    if (set(document.keys()).intersection(required_fields) == set(required_fields)):
        sum += 1
print(sum)

# Part 2
sum = 0
for document in documents:
    # “lazy evaluation” with and makes this condition "safe"(?)
    if (set(document.keys()).intersection(required_fields) == set(required_fields)) and check_validity(document):
        sum += 1
print(sum)

