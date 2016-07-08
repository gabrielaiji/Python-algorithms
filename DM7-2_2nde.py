from math import cos

print ()
print ()

x = float(input("Point de départ ? "))

i = 0

while int(x * 10**9) != int(cos(x) * 10**9):
#while abs(x - cos(x)) > 10**(-9):
	x = cos(x)
	i += 1

	print (i)
	print (x)
	print ()
	print ()

print ()
print ("Beta : ", x )
print ("Nombre de réitérations : ", i)
