#this is a class to define a full clue. It includes the total number of letters, the block,
#the block's location by index, and any cocnnections to other clues.
#it keeps track of which clue is which by an auto-incrementing id
#actually, I can just use the built in id function. Go Python!
#actually, I need to keep track of ID by hand because I don't
#want to get into any problems where the ID isn't what I think it's going to be.
#since I have to number the clues anyway to input them into the text file, 
#it's better to just use my own ID numbers and be done with it.
#however, I need to figure out the pointer problem if I don't want to destroy my runtime

import sys

class Clue:
	def __init__(self, id, length, blockStartIndex, block, connections):
		self.id = id
		self.length = length
		self.blockStartIndex = blockStartIndex
		self.block = block
		self.connections = connections
		self.solved = False
		self.potentialSolutions = self.getPotentialSolutions() #potential solutions are solutions that don't take connections into account. I'll deal with that problem later

	def print(self):
		if self.solved:
			# solutionFirstHalf = self.potentialSolutions[0][0:self.blockStartIndex]
			# solutionSecondHalf = self.potentialSolutions[0][(self.blockStartIndex + 2):]
			# print (self.solutionFirstHalf, self.block.print(), self.solutionSecondHalf)
			print("Clue",self.id,"solution is",self.potentialSolutions[0][:-1],"to block", self.block.print(),"at index",self.blockStartIndex)
		else:
			print ("Not solved yet! " + "the block ", self.block.print(), " is at index " , self.blockStartIndex )
			print ("The potential solutions are: " , self.potentialSolutions)

#definitely potential for refactoring here, right now I'm just going to split the database into
#a bunch of databases based on word length and search through it to find potential solutions
#not really  very good solution, but can always come back and refactor pretty easily. Maybe I'll
#implement a trie and have it search through that, that'll cut down the runtime from O(ND)
#where N is the number of clues and D is the size of the database
#in practice though, even though this is the bottleneck, splitting the database by word length 
#lessens the actual max number of calculations done per clue to about 15k per clue (there are about 100K words in my database,
# and a quick google tells me that the highest concentration of word lengths in the english language is 14% at 9 letters),
#which isn't astronomically bad
	def getPotentialSolutions(self):
		index = self.blockStartIndex
		top = self.block.top
		bottom = self.block.bottom
		databaseName = "words" + str(self.length) + ".txt"
		#print(databaseName)
		try:
			readFile = open(databaseName)
		except:
			print("The database doesn't exist. You need to run CreateDatabase.py first, then try this again.")
			sys.exit()

		allWords = readFile.readlines()
		readFile.close() #it's only polite to close the file when you're done with it

		topSolutions = [] #list of words that have the top in the right place
		bottomSolutions = [] #list of words that have the bottom in the right place
		for i in allWords:
			#print(i,"-",top,"-",bottom)
			#print("Top[0]",top[0])
			#print("Index:",index)
			if (i[index] == top[0].lower()) and (i[index+1] == top[1].lower()):
				topSolutions.append(i) # = topSolutions + i
				#print("TopSolutions: ",topSolutions)
			else:
				if (i[index] == bottom[0].lower()) and (i[index+1] == bottom[1].lower()):
					bottomSolutions.append(i) # = bottomSolutions + i
					#print("BottomSolutions: ",bottomSolutions)
		#now I should have lists of words that match the top half of the block and the bottom half of the block
		#print("TopSolutions: ", topSolutions)
		#print("BottomSolutions:", bottomSolutions)
		potentialSolutions = []
		#compare the lists 
		#this is also a horrible way to compare lists
		for topWord in topSolutions:
			for bottomWord in bottomSolutions:
				isMatch = True
				for (i, letter) in enumerate(topWord):
					#compare the part of the word before and after the block
					if (i < index or i > index + 1) and topWord[i] != bottomWord[i]:
						isMatch = False 
				if isMatch:
					potentialSolutions.append(topWord) # = potentialSolutions + topWord
					break #should stop looking through bottomWords once it finds a match, and move on to the next topWord
		#print("PotentialSolutions:",potentialSolutions)
		return potentialSolutions

				



