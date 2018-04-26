#this is a class to define the 4 letter block within the clue.
#pretty straightforward, self explanatory

class Block:
	def __init__(self, top, bottom):
		self.top = top
		self.bottom = bottom
	
	def print(self):
		return "[ " + self.top + " | " + self.bottom + " ]"
		#print ( "[" , self.top , "," , self.bottom + " ]" )
	