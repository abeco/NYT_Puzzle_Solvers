
import sys

from NewPuzzle import NewPuzzle

puzzle = NewPuzzle()
if(len(sys.argv) > 1):
	print(sys.argv[1])
else:
	print("Please run this program again with a .txt file as a command line argument.")
	exit(0)



input = str(sys.argv[1])
if(input[-4:] != ".txt"):
	print(input[-4:])
	print("Please run this with a .txt file")
	exit(0)
else:
	try:
		f = open(input, "r")
	except:
		print("Could not open file")


puzzle.readIn(input)
puzzle.solve()
puzzle.print()
