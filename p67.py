x = input('Enter an integer: ')
print(x)

def square(num):
	if not str(num).isdigit():
		return 'Invalid entry!'
	num = int(num)
	return num * num

result = square(x)

print('Original:\t', x, '\tSquared:\t', result)

