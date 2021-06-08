def incrementer():
	i = 1
	while True:
		yield i
		i += 1

inc = incrementer()

print(next(inc))
print(next(inc))
print(next(inc))
print(next(inc))

counter = incrementer()

for i in range(20):
	print(next(counter))
	
print(next(inc))

