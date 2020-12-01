#!/usr/bin/python3

# Python3 Program for recursive binary search. (found at: https://www.geeksforgeeks.org/binary-search/)
# Returns index of x in arr if present, else -1 
def binarySearch (arr, l, r, x): 
	if r >= l: 
		mid = l + (r - l) // 2
		if arr[mid] == x: 
			return mid 
		elif arr[mid] > x: 
			return binarySearch(arr, l, mid-1, x) 
		else: 
			return binarySearch(arr, mid + 1, r, x) 
	else: 
		return -1

puzzle = sorted([ int(value.rstrip('\n')) for value in open('input.txt', 'r').readlines()])

for element in puzzle:
    magic_number = 2020 - element
    if (binarySearch(puzzle, 0, len(puzzle)-1, magic_number) != -1):
        print(element * magic_number)
        break