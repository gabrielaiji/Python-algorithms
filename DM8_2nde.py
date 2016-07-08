from math import sin
from math import pi

print ()
print ()

a = 1
x = a / 2
y = 1 - sin(x)

while int(x * 10**5) != int(y * 10**5):
	if x - y > 0 :
		a -= (a/2)

	elif x - y < 0 :
		a += (a/2)


	x = a / 2
	y = 1 - sin(x)

print ("alpha :")
print ( a, "radians")

a = a *(180/pi)
print (a , "degrés")

a = (a - int(a))* 60
print (a, "minutes")

a = (a - int(a)) *60
print (a , "secondes")