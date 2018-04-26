#this is the file you run to split the list of english words by length. Don't look, you might vomit.


print("started main execution")
inFile = "wordsEn.txt"
#try: 
readFile = open(inFile)
#except:
#	print("Please make sure wordsEn.txt is in this directory")
allWords = readFile.readlines()
print("read all the lines")
readFile.close()

#I know, this is really stupid. But who cares? I'm only running this once, and hopefully I remember to refactor this before anyone sees how terrible it is
#I'm also making the assumption that any clue longer than 12 letters is way too difficult and would never happen.
#The longest clue I've encountered is 7 letters long, so I think I'm safe.
with open('words3.txt', 'a') as words3,	\
open('words4.txt', 'a') as words4, 	\
open('words5.txt', 'a') as words5, 	\
open('words6.txt', 'a') as words6, \
open('words7.txt', 'a') as words7, 	\
open('words8.txt', 'a') as words8, \
open('words9.txt', 'a') as words9, \
open('words10.txt', 'a') as words10, \
open('words11.txt', 'a') as words11, \
open('words12.txt', 'a') as words12:
	for word in allWords:
		#print( word + " length: " + str(len(word)))
		length = len(word) - 1 #it comes with an endline character
		if length == 3:
			words3.write(word)
		elif length == 4:
			words4.write(word)
		elif length == 5:
			words5.write(word)
		elif length == 6:
			words6.write(word)
		elif length == 7:
			words7.write(word)
		elif length == 8:
			words8.write(word)
		elif length == 9:
			words9.write(word)
		elif length == 10:
			words10.write(word)
		elif length == 11:
			words11.write(word)
		elif length == 12:
			words12.write(word)

# words4 = []
# words5 = []
# words6 = []
# words7 = []
# words8 = []
# words9 = []
# words10 = []
# words11 = []
# words12 = []
#I hate myself more and more the more I write this abysmal code. This is decidedly un-DRY. 
		

words3.close()
words4.close()
words5.close()
words6.close()
words7.close()
words8.close()
words9.close()
words10.close()
words11.close()
words12.close()

print("eof")