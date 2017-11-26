import json
import BeehiveFunctions

def main():

	letterDict = {}
	wordDict = {}
	onesLetterDict = {}
	
	letterDB = 'BeehiveLetterDB.txt'
	wordDB = 'BeehiveWordDB.txt'
	onesLetterDB = 'BeehiveOnesLetterDB.txt'

	with open(letterDB) as infile:
		letterDict = json.load(infile)

	with open(wordDB) as infile:
		wordDict = json.load(infile)
	#with open(onesLetterDB) as infile:
	#	onesLetterDict = json.load(infile)

	central = [input("Please enter central letter: ")]
	while BeehiveFunctions.valid_input(central, 1) == False:
		central = [input("Please enter one letter: ")]
	outsideLetters = [str(x) for x in input("Next enter the other letters, separated by spaces: ").split(" ")]
	while BeehiveFunctions.valid_input(outsideLetters, 6) == False:
		outsideLetters = [str(x) for x in input("Please enter 6 letters, separated by spaces: ").split(" ")]
	inputLetters = BeehiveFunctions.concatenate_lists(central, outsideLetters)
	#now i have a list of all the letters in the puzzle
	threePointWords =  BeehiveFunctions.threes(letterDict,inputLetters)
	if len(threePointWords) > 0:
		threeKeyword = threePointWords[0]
		onePointWords = BeehiveFunctions.ones(wordDict[threeKeyword],central)
	else:
		with open(onesLetterDB) as infile:
			onesLetterDict = json.load(infile)
		onePointWords = BeehiveFunctions.ones_no_threes(onesLetterDict, inputLetters)

	return(threePointWords, onePointWords)


def print_main(tuple):
	print("Three Point Words:")
	for i in tuple[0]:
		print(i)
	if len(tuple[0]) == 0:
		print("None")
	print("One Point Words:")
	for i in tuple[1]:
		print(i)
	if len(tuple[1]) == 0:
		print("None")	


boolean = True

while(boolean):
	returnValue = main()
	print_main(returnValue)
	another = input("Want to crack another puzzle? Enter Y or N: ")
	yes = ["Y", "y", "yes"]
	if not BeehiveFunctions.subset(another, yes):
		boolean = False
print("Goodbye")