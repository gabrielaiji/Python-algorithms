from random import choice

abcsisse = abs(int(input("Abscisse : ")))
n = abs(int(input("Nombre de simulation(s) : ")))

s = 0

for i in range(n):
	a = 0
	p = 0
	while p == 0:

		if a == abcsisse or a == -abcsisse:
			p = 1
			break

		s += 1

		saut = choice([1, -1])
		a += saut

print (s/n)
