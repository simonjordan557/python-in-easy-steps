import dog

for i in dir(dog):
	print(i)

for j in dir(dog.__builtins__):
	print(j)


for k in dir(dog.__cached__):
	print(k)
