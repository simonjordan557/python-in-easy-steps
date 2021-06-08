class Bird:
	'''A base class to define bird properties.'''
	
	count = 0
	
	def __init__(self, chat):
		Bird.count += 1
		self.sound = chat

	def talk(self):
		return self.sound
