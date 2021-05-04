callbacks = [ lambda x : x **2, lambda x : x ** 3, lambda x : x**4 ]

print('\nAnonymous Lambda functions:')
for func in callbacks:
	print('Result:', func(2))

def poweroftwo(x) :
	return x ** 2

def powerofthree(x) :
	return x ** 3

def poweroffour(x) :
	return x ** 4

morecallbacks = [poweroftwo, powerofthree, poweroffour]

print('\nNamed Def functions:')
for f in morecallbacks:
	print('Result:', f(3))
