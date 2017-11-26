import json
import BeehiveFunctions

#now that I think of it, I should've made these functions able to run separately
#but since I only needed to run this once to initially create the database, it doesn't really matter

source = 'wordsEn.txt' #text file containing every word in the english language
f = open(source)

allWords = f.readlines()

for (i, item) in enumerate(allWords):
	allWords[i] = item[:-1]
#since the file I got contains endline characters, I'll need this to quickly edit the list

letterDBdict = {} #dictionary to be used to find the 3-point word(s) associated with the provided letters
threes = [] #list of all 3-point words; words that use exactly 7 letters
ones = [] #list of all potential 1-point words; words that have length >= 5 and use < 7 letters
temporaryOnesLetterDict = {} #used to create wordDBdict

for (i, item) in enumerate(allWords):
	letters = [] #for each word, this will serve as the set of its letters
	for j in item:
		if j not in letters:
			letters.append(j)
	#print(letters)
	if len(letters) == 7:
		#print('qualifies for threes')
		threes.append(item)
		letterDBdict[item] = sorted(letters)
	elif len(item) >= 5 and len(letters) < 7:
		#print('qualifies for ones')
		ones.append(item)
		temporaryOnesLetterDict[item] = sorted(letters)
print('created letterDBdict')
wordDBdict = {} #dictionary to be used for finding associated 1-point words from 3-pointers
#once a function returns all associated 1-point words, or the correct value in this dictionary,
#the script can then sort through that short list to filter out words without the central letter

for key, value in letterDBdict.items():
	associated = [] #this list is of all the ones associated with each three
	for keyOne, valueOne in temporaryOnesLetterDict.items():
		#if valueOne.issubset(value): #not a thing, easy way just make a new function to compare the lists
		if BeehiveFunctions.subset(valueOne,value):
			associated.append(keyOne)
	wordDBdict[key] = sorted(associated)
print('created wordDBdict')
#now that the dictionaries for the database are created, I'm gonna store them in text file using json
#to preserve the dictionary format. In the main script, I'll retrieve them instead of having to
#regenerate them each time a search is done. That would take a stupid amount of time

with open('BeehiveLetterDB.txt', 'w') as outfile:
	json.dump(letterDBdict, outfile)

with open('BeehiveWordDB.txt', 'w') as outfile:
	json.dump(wordDBdict, outfile)
with open('BeehiveOnesLetterDB.txt', 'w') as outfile:
	json.dump(temporaryOnesLetterDict, outfile)

print('eof')