name = input("What is your name? ")
for n in name :
	print(n, sep = '', end = "!\n")

print("\n")

games = { "Exed Exes" : "Famicom", "Strikers 1945" : "PS1", "Gunhed" : "PC Engine" }
for g in games:
	print(g)

print("\n")

for key, value in games.items():
	print(key, "is on", value)

print("\n")

for i in range(5):
	print(i)

print("\n")

for i in range(1, 10, 2):
	print(i)

chars = ['A', 'B', 'C']
fruit = ('Apple', 'Banana', 'Cherry')
dict = {'name' : 'Mike', 'ref' : 'Python', 'sys' : 'Win'}

print('\nElements:\t', end = ' ')
for item in chars:
	print(item, end = ' ')

print('\nEnumerated:\t', end = ' ')
for item in enumerate(chars):
	print(item, end = ' ')

print('\nZipped:\t', end = ' ')
for item in zip(chars, fruit):
	print(item, end = ' ')

print('\nPaired:\t', end = ' ')
for key, value in dict.items():
	print('(',key, '=', value, ')',  end = ' ')

print('\n')

