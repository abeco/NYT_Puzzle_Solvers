from Clue import Clue
from Block import Block
import sys

class NewPuzzle:

	def readIn(self, inputFile):
		clues = []
		#gotta do responsible file io
		try:
			inputPuzzle = open(inputFile)
		except (IOError, FileNotFoundError) as e:
			print ("Could not read file: ", inputFile)
			sys.exit(0)
		
		with inputPuzzle:
			clueIDs = []
			allClues = inputPuzzle.readlines()
			for clue in allClues:
				clueElements = clue.split()
				#print("ClueElements: ", clueElements)
				try:
					id = int(clueElements[0])
					length = int(clueElements[1])
					bsi = int(clueElements[2])
				except (TypeError, ValueError) as e:
					print("Clue ",clue," is not formatted correctly.")
					sys.exit()
				
				#checks if you repeated IDs
				for clueID in clueIDs:
					if(id == clueID):
						print("You repeated ID ",id)
						sys.exit()

				#checks the clue length
				if(length < 3 or length > 12):
					print("Clue ",clue," has an invalid length")
					sys.exit()

				#checks the bsi
				if(bsi > (length - 2) or bsi < 0):
					print("Clue ",clue," has a Block Start Index that's out of bounds")
					sys.exit()
				#Clue constructor: id, length, blockStartIndex, block, connections
				#first read in the block and connections, then call clue constructor
				if( (len(clueElements[3]) == 2) and (len(clueElements[4]) == 2) 
					and (clueElements[3].isalpha()) and (clueElements[4].isalpha()) ):
					clueBlock = Block(clueElements[3], clueElements[4])
				else:
					print("The block in clue ",clueElements[0]," is not formatted correctly")
					sys.exit()
				#gonna be at least one connection, because a puzzle of one clue is dumb
				#might as well check tho
				if len(clueElements) < 6:
					print ("Clue ",clueElements[0]," doesn't have the correct formatting.")
					sys.exit()
				#also don't want an out of bounds error, double check so not off by one
				clueConnections = []
				for i in range(5, len(clueElements) - 1,2):
					try:
						connection = (int(clueElements[i]), int(clueElements[i+1]))
						if(connection[1] == (bsi + 1) or connection[1] == (bsi)):
							print("Clue ",id," has a connection inside the block")
							sys.exit()
					except (TypeError, ValueError) as e:
						print("A connection on clue ",id," doesn't have the correct formatting")
						sys.exit()
					clueConnections.append(connection)
				for i in clueConnections:
					for j in clueConnections:
						if(i[1] == j[1] and j != i):
							print("Clue ",id," has two connections at the same index",i[1])
							sys.exit()
				#now that I have all the pieces, call Clue and append it to master list
				currentClue = Clue(id, length, bsi, clueBlock, clueConnections )
				clues.append(currentClue)

		self.clues = clues

	#see whittle in back of blue notebook
	#this basically just in version one finds the first clue that has only one potential solution
	#and in version two decides whether to call whittle or reverse whittle on the first clue
	def solve(self):
		# self.__reverseWhittle(self.clues[0])

		for clue in self.clues:
			if len(clue.potentialSolutions) == 1:
				clue.solved = True
				print("Clue",clue.id,"can be solved immediately. Its solution is",clue.potentialSolutions[0][:-1])
				self.__whittle(clue)

		print("Complete Puzzle solved")
		
	#always gonna call whittle on a solved clue
	def __whittle(self, clue):
		print("Whittling clue", clue.id)
		clueSolution = clue.potentialSolutions[0]
		for connection in clue.connections:
			#find the clue and where they're connected. Could be constant time with pointers, for now it's O(clues)
			connectedClue = self.__findConnectedClue(connection)
			primaryConnectionIndex = connection[1]
			secondaryConnectionIndex = self.__findSecondaryConnectionIndex(connectedClue, clue.id)

			if not connectedClue.solved:
				for word in connectedClue.potentialSolutions:
					#remove anything from connectedClue's potential solutions that doesn't match with the solved clue
					if clueSolution[primaryConnectionIndex] != word[secondaryConnectionIndex]:
						connectedClue.potentialSolutions.remove(word)

				if len(connectedClue.potentialSolutions) == 1:
					#mark it solved and start whittling the connected clue
					connectedClue.solved = True
					print("Clue", connectedClue.id, "solution is", connectedClue.potentialSolutions[0][:-1])
					self.__whittle(connectedClue)

				elif len(connectedClue.potentialSolutions) == 0:
					#if all the potential solutions are eliminated, exit gracefully
					print("Clue ", connectedClue.id,"has no solution.")
					sys.exit()
				else:
					#if, after whittling there still exists multiple potential solutions because it relies
					#on another connection to be solved, reverse whittle the connected clue to solve it	
					print("Couldn't solve clue ", connectedClue.id,"by whittling. Starting to reverse whittle.")
					print("Its potential solutions are: ",connectedClue.potentialSolutions)
					self.__reverseWhittle(connectedClue, False)

	#call this on whittled clue that still isn't solved
	#or on the first clue if it needs its connections to get solved
	def __reverseWhittle(self, clue, calledFromReverseWhittle):
		#don't reverse whittle a solved clue. That's pointless and dumb and could fuck shit up for you
		if clue.solved == True:
			print("Reverse whittle was called on a solved clue. Terminating thread")
			#self.__whittle(clue)
		else:
			#get a connected clue for later
			connectedClue = self.__findConnectedClue(clue.connections[0])
			print("Reverse Whittling clue", clue.id)
			for connection in clue.connections:
				#get the connection data
				connectedClue = self.__findConnectedClue(connection)
				primaryConnectionIndex = connection[1]
				secondaryConnectionIndex = self.__findSecondaryConnectionIndex(connectedClue, clue.id)

				if connectedClue.solved:
					#remove anything from the original clue's potential solutions that doesn't fit with the connections
					for word in connectedClue.potentialSolutions:
						for potentialSolution in clue.potentialSolutions:
							if potentialSolution[primaryConnectionIndex] != word[secondaryConnectionIndex]:
								#print("Potential Solution",potentialSolution[:-1],"doesn't match",word[:-1],"at",primaryConnectionIndex,"and",secondaryConnectionIndex)
								#print("Removing", potentialSolution[:-1])
								clue.potentialSolutions.remove(potentialSolution)

			
			if len(clue.potentialSolutions) == 1:
				#mark it solved and whittle it, solving its connections
				clue.solved = True
				print("Clue",clue.id,"solution is",clue.potentialSolutions[0][:-1])
				self.__whittle(clue)
			elif len(clue.potentialSolutions) == 0:
				#exit gracefully
				print("Clue",clue.id,"has no solution")
				sys.exit()
			else:
				if calledFromReverseWhittle == False:
					print("Reverse whittling clue",clue.id,"didn't work. Reverse whittling clue",connectedClue.id)
					self.__reverseWhittle(connectedClue, True)
				else:
					print("Reverse whittling",clue.id,"again didn't work. Terminating thread")
				#reverseWhittle last connected clue

	#this one needs to return a Clue object
	#also this is apparently how you signal a private function. It's more of a "private" function, because
	#real privacy doesn't exist in python
	def __findConnectedClue(self, connection):
		for clue in self.clues:
			if clue.id == connection[0]:
				return clue

	#this one needs to return an int
	#pass in connectedClue, clue.id 
	def __findSecondaryConnectionIndex(self, clue, connectionID):
		for connection in clue.connections:
			if connection[0] == connectionID:
				return connection[1]

	def print(self):
		for clue in self.clues:
			clue.print()



