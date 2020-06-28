def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def convert(liste): 
    return list(i for i in liste) 

def trace(wire, head):
	liste = []
	for x in wire:
		if x[0] == 'R':
			for i in range(int(x[1:])):
				head[0] += 1
				liste.append(head.copy())
		elif x[0] == 'L':
			for i in range(int(x[1:])):
				head[0] -= 1
				liste.append(head.copy())
		elif x[0] == 'U':
			for i in range(int(x[1:])):
				head[1] += 1
				liste.append(head.copy())
		elif x[0] == 'D':
			for i in range(int(x[1:])):
				head[1] -= 1
				liste.append(head.copy())
	return liste

f = open("input.txt","r")
liste = []

wire1 = f.readline().rstrip("\n").split(",")
wire2 = f.readline().rstrip("\n").split(",")

head1 = [0,0]
head2 = [0,0]

lst1 = trace(wire1, head1)
lst2 = trace(wire2, head2)

lst1 = [tuple(l) for l in lst1]
lst2 = [tuple(l) for l in lst2]

inter = intersection(lst1, lst2)

listeliste = []

for h in inter:
	listeliste.append(lst1.index(h) + lst2.index(h) + 2)
	pass
print(min(listeliste))