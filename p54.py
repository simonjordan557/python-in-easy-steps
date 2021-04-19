a = 1
while a < 20 :
	print(a)
	a += 1
print("All Done! a =", a)

b = 0
while b < 20 :
	b += 1
	if (b == 10) :
		continue
	print(b)
print("All Done! b  =", b)
 	
c = 0 
while (c < 20) :
	c += 1
	if (c > 15) :
		break
	print(c)
print("All Done! c =", c)

i = 1
while i < 4 :
	print("\nOuter Loop Iteration:", i)
	i += 1
	j = 1
	while j < 4 :
		print("\tInner Loop Iteration:", j)
		j += 1

def fib() :
	y, z = 0, 1
	while y < 100 :
		print(y)
		y, z = z, y + z

fib()
