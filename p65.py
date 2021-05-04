def echo(user):
	print('User:\t', user)

# name = input("What is your name? ")
# echo(name)

echo(input('What is your name? '))

def echo(user, lang, sys):
	print('User:\t\t', user, '\nLanguage:\t', lang, '\nSystem:\t\t', sys)

echo('Simon', 'Python', 'Linux')
# echo('Nicola') won't work, the original echo function has now been superseded, function overloading doesn't seem to be supported?
# Arguments can be passed in different order if explained in the call:
echo(sys = 'OSX', lang = 'Swift', user = 'Emily')

# Default values can be supplied to facilitate overloading!

def mirror(user = 'Anon', lang = 'Python', sys = 'Windows'):
	print('User:\t\t', user, '\nLanguage:\t', lang, '\nSystem:\t\t', sys) 


mirror()
mirror(lang = 'Java')
mirror(user = 'Tony')
mirror('One')
mirror('One', 'Two')
mirror('One', 'Two', 'Three')
