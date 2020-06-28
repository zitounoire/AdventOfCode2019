def trace(wire, head):
	liste = []
	for x in wire:
		if x[0] == 'R':
			for i in range(int(x[1:])):
				head[0] += 1
				liste.append(head.copy())
				pass
			pass
		elif x[0] == 'L':
			for i in range(int(x[1:])):
				head[0] -= 1
				liste.append(head.copy())
				pass
			pass
		elif x[0] == 'U':
			for i in range(int(x[1:])):
				head[1] += 1
				liste.append(head.copy())
				pass
			pass
		elif x[0] == 'D':
			for i in range(int(x[1:])):
				head[1] -= 1
				liste.append(head.copy())
				pass
			pass
	return liste
	pass

f = open("input.txt","r")
liste = []

wire1 = f.readline().rstrip("\n").split(",")
wire2 = f.readline().rstrip("\n").split(",")

head1 = [0,0]
head2 = [0,0]

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


def convert(liste): 
    return list(i for i in liste) 

lst1 = trace(wire1, head1)
lst2 = trace(wire2, head2)

lst1 = [tuple(l) for l in lst1]
lst2 = [tuple(l) for l in lst2]

lst1 = convert(lst1)
lst2 = convert(lst2)

inter = intersection(lst1, lst2)

def taxicabDistance(xA,yA,xB,yB):
  distance = abs(xA-xB) + abs(yA-yB)
  return distance

lst1 = list(dict.fromkeys(lst1))
lst2 = list(dict.fromkeys(lst2))

listeliste = []

for h in inter:
	listeliste.append(taxicabDistance(0,0,h[0],h[1]))
	pass
print(min(listeliste))