'''

	XXX

'''

'''Contains the brick class'''

class brick():

	def __init__(self, ty, x, y):
		'''Initialization'''
		if ty == 'breakable':
			self.breakable = True
		else:
			self.breakable = False
		self.posX = x
		self.posY = y
