class Critter:
	'''A base class for all critter properties.'''

	count = 0

	def __init__(self, chat):
		self.sound = chat
		Critter.count += 1

	def talk(self):
		return self.sound
