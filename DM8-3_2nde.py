from math import sin

def fact(x):#factorielle
	x = int(abs(x))
	y = x

	while x > 1:
		x -= 1
		y = y * x
		
	return y

def S(i):#Sn fonction sin(1)
	y = abs(1 + 2*(i-1))
	y2 = 1
	x = 1
	p = 1

	while y != y2:
		p *= -1
		y2 += 2
		if p == -1:
			x -= 1 / fact(y2)

		elif p == 1:
			x += 1 / fact(y2)

		else:
			print("Error")
			break
				
	return x


print ()

n = 0

while int(sin(1)* 10**9) != int(S(n) * 10**9):
	n += 1

print()
print(n)
