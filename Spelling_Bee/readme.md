This is a puzzle solver written for the New York Times puzzle called Spelling Bee. This is a description of the game and the solver.
Game(Text straight from NYT): How many common words of 5 or more letters can you spell using the letters in the hive? Every answer must use the center letter at least once. Letters may be reused in a word. At least one word will use all 7 letters. Proper names and hyphenated words are not allowed. Score 1 point for each answer, and 3 points for a word that uses all 7 letters.
     C
  R     E
     Y
  O     M
     N 

In this case, Y is the central letter. The 3 point example would be 'ceremony', and a few valid 1 point words would be money, corny, mercy, etc. 

run the solver in the command line with 'python BeehiveMain.py'. It will then prompt you for the central letter, followed by the other letters. Then it will tell you the 3 point words, followed by the one point words. 

I know, not the best way to run this, off the bat I could improve this by just using command line arguments. I'll do that. Also I need to add more robust error handling, but for now it's fine. 

Solver Logic: So the way this solver works is first, I ran Beehive.py to create the database that BeehiveMain uses.

Beehive is very well commented, so feel free to look there to see how I created the dictionaries that BeehiveMain looks through. Basically the end result is that BeehiveMain looks through a list of all potential three point words and finds the words that work for the given input letters. It then takes the first three point word (any three works, so I just take the first) and checks a dictionary that has it mapped to all words that can be made from its letters, and sorts out the ones that use the central letter. 

Potential improvements: 
-Can put the threes in a hash table for constant lookup instead of O(N) lookup to find the list of threes
-Same with the next dictionary that maps all threes to their potential ones
-Command Line inputs