import unittest
from NewPuzzle import NewPuzzle

class BadFileTest(unittest.TestCase):
	def test(self):
		puzzle = NewPuzzle()
		with self.assertRaises(SystemExit):
			self.assertEqual("Could not read file: badfile.txt", puzzle.readIn("badfile.txt"))

class ClueInputTest(unittest.TestCase):
	def testBlockFormatType(self):
		puzzle = NewPuzzle()
		with self.assertRaises(SystemExit):
			self.assertEqual("The block in clue 1 is not formatted correctly", puzzle.readIn("testpuzzles/test1.txt"))
	def testBlockFormatLength(self):
		puzzle = NewPuzzle()
		with self.assertRaises(SystemExit):
			self.assertEqual("The block in clue 1 is not formatted correctly", puzzle.readIn("testpuzzles/test2.txt"))
	
	def testClueFormatLength(self):
		puzzle = NewPuzzle()
		with self.assertRaises(SystemExit):
			self.assertEqual("Clue 1 doesn't have the correct formatting.", puzzle.readIn("testpuzzles/test3.txt"))
	
	def testIDType(self):
		file  = open("test3.txt", "w")
		file.write("R 4 0 IN EA 2 2")
		file.close()
		puzzle = NewPuzzle()
		with self.assertRaises(SystemExit):
			self.assertEqual("Clue R 4 0 IN EA 2 2 is not formatted correctly.", puzzle.readIn("test3.txt"))
# 	def testIDRepeat(self):

	def testBadBSI(self):
		file  = open("test3.txt", "w")
		file.write("1 4 3 IN EA 2 2")
		file.close()
		puzzle = NewPuzzle()
		with self.assertRaises(SystemExit):
			self.assertEqual("Clue 1 has a Block Start Index that's out of bounds", puzzle.readIn("test3.txt"))
	def testBadLength(self):
		file  = open("test3.txt", "w")
		file.write("1 2 3 IN EA 2 2")
		file.close()
		puzzle = NewPuzzle()
		with self.assertRaises(SystemExit):
			self.assertEqual("Clue 1 has an invalid length", puzzle.readIn("test3.txt"))

		
	def testRepeatedConnectionIndex(self):
		file  = open("test3.txt", "w")
		file.write("1 2 3 IN EA 2 2 4 2")
		file.close()
		puzzle = NewPuzzle()
		with self.assertRaises(SystemExit):
			self.assertEqual("Clue 1 has two connections at the same index", puzzle.readIn("test3.txt"))

		
# class PuzzleInputTests(unittest.TestCase):
# 	#what if there's no immediately solvable clue?
# 	def noSolvableClue(self):

# 	def noReciprocalConnection(self):

# 	def clueReferencedDoesntExist(self):

# 	def unsolvableClue(self):
	
	
