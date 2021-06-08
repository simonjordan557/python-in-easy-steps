text = 'The political slogan "Workers Of THe World Unite!" is from The Communist Manifesto.'
with open('update.txt', 'w') as file:
	file.write(text)
	print('\nFile now closed?', file.closed)
print('File now closed?', file.closed)

with open('update.txt', 'r+') as file:
	text = file.read()
	print('\nString:', text)
	print('\nPosition in file now:', file.tell())
	file.seek(33)
	print('\nPosition in file now:', file.tell())
	file.write('All Lands')
	file.seek(59)
	file.write('the tombstone of Karl Marx.')
	print('\nPosition in file now:', file.tell())
	file.seek(0)
	text = file.read()
	print('\nString:', text)
