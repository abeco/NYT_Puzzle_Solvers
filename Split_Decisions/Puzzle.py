#not done. This needs a bit more work
#only thing that needs to be done is to figure out matching and fix Clue's print function
#this is a class to define a full puzzle. It's got a list of clues (which themselves 
# store their connections to other clues), a solve function, and a print function
# so that basically all the main program has to do to execute is create a puzzle,
# puzzle.readIn("puzzle.txt") puzzle.solve(), and puzzle.print()
# can even skip a step and just put the reading in in the constructor
# but if it's a command line arg anyway, no point in making it more difficult
# See readme for puzzle.txt formatting

#matching: The first way I'm thinking to do it is to work off of the one-PS clues.
#ex. the only one that matched purple was chirp, and the only one that matched chirp was inch
#the problem is, there has to be at least one clue that you can get without the connections
#also, I should look into making that recursive in some way. 
#basically the move would be to just call solve on all the connections of the first clue that only had 
#one potential solution, mark the solved clues solved, and keep going until all the clues were solved.
#this is where it turns into a graph traversal.
#I think breadth-first works best here. Say purple has more than one connection: I'd want to whittle down the 
#list of potential solutions to things that match with purple before continuing on to that clue's other solutions.
#what if there's more than one thing that works with purple? Then what? You'd go through that connections
#potential solutions and its connections, so let's say chirp and xhirp work with purple. Xhirp wouldn't have any solutions with
#the other connection, so it could be eliminated. I don't have to worry about there being multiple solutions if it's a valid puzzle
#the thing is, I feel like that method's gotta work even if you don't start with a 1ps clue. If it recurses through, it should
#go something like: 1's matches: inch -> chirp , inst -> spire. spiry ; unsolved. 2's matches to connection at 4: chirp -> purple.
#chirp is the solution. is there any connected clue that's unsolved? Yes, 1. What matches with chirp? Inch, now it's solved.
#come to think of it, this sounds like depth first search now that I talk it out.

#let's say you whittle a clue down and it's still not solved because it needs it's other connections to solve it.
#then what do you do? ex. say chirp and xhirp both worked with purple. Then you'd need to reverse whittle clue 2.
#by reverse whittle I mean do the exact same thing, but instead of deleting the non-matching words from the connected clue and solving that,
#you'd delete the words from the original clue's list, and then it would be solved. Then you could call whittle on the original and continue 
#execution as usual

#something just dawned on me, if you start with a reverse whittle, you can get rid of the requirement that the puzzle
#has to have one clue that can be solved without whittling. For example. You reverse whittle clue 1, it doesn't help you. Neither clue 1 nor clue 2 are solved
#so you reverse whittle clue 2. That solves clue 2. (What if that doesn't solve clue 2?) So then you can call whittle on clue 2 and that solves clue 1 and clue 3. You now whittle clue 1, all its connections
# are solved so it doesn't do anything and it finishes, and it 'solves' clue 3, calls whittle on it and the same thing happens, so it exits the recursion
# and now the puzzle is solved, so you can print it.

#what if that doesn't solve clue 2? Then you can potentially have an infinite loop on your hands if it then reverse whittles clue 1 again.
#you have to 1. either call reverse whittle on another one of 2's connections 2. quit the branch execution and hope the program comes back to it when one of the clues is solved
#
#(which it should. if it doesn't, then you can always come back to it during the check at the end of solve)
#but if it happens at the beginning of execution when there aren't any other branches, that wouldn't solve the puzzle. So I need to come up with the comprehensive solution for this
#either way, should modify the function and call reverseWhittle with a calledFromReverseWhittle boolean 

#no so you still need a clue that can be solved by itself, because reverse whittling depends on the connections being solved, and only then can you
#eliminate a potential solution based on a mismatch

#speaking of, I need to find a good way to print it now that I don't have a solutionFirstHalf and solutionSecondHalf
#I can just generate a solFirstHalf and secondHalf in the print function from the solution and print it from there

#so the infinite loop problem only arises if a reverseWhittle called from a reverseWhittle doesn't solve the clue. When reverseWhittle calls reverseWhittle, it calles it on the
#last connection. So the problem only arises if it's the last connection in both, they're both unsolved (obviously), and the answer can only be obtained by a single one of the two clues' connections
#Solution: if a reverseWhittle is called from another reverseWhittle, and it doesn't solve the second clue, call reverse whittle on one of the other connections.
#Can this problem be fixed by just calling it with the first connection? If the clue only has one connection then it can't not be solved by a reverse whittle -- unless the other clue isn't solved


#new idea: if you try to reverse whittle something and it doesn't get solved, then you reverse whittle the connection and that does get solved, the original clue should get solved by reverse whittling.
#So if something was already visited by reverse whittle, you shouldn't try reverse whittling it again. I think that's fine. I need to test it and see if I can improve this for the case where
#the infinite loop happens too early in the execution. What's too early in the execution? 

#what if I keep track of the reverse whittling chain? So every time reverse whittle gets called from whittle(or the start), it gets called with a new chain.
#if it's already been reverse whittled on the chain, quit execution because that's the indicator of an infinite loop

#Plan 2.0: There's two ways to solve an infinite loop problem, and now that I think about it, there's two ways to solve any problem:
#Deal with it, or avoid it. While it may not be the most sound life advice, I'm gonna go with the latter here, if only because it feels
#a lot easier than the former, again, not unlike real life. I'm gonna do this really simply with two tactics:
#1. When a reverse whittle that's called by a reverse whittle doesn't solve the problem (since this is an imperfect way to deal with the problem in general),
#just terminate the execution thread. This is only a real problem if this happens in the beginning of the execution and the program doesn't have any 'loose ends',
#or waiting-to-be-executed recursive calls in the stack. (It'll happen in the beginning of my test puzzle, and any other puzzle that doesn't start with a onePS)
#2. This flaw is solved by starting execution somewhat similarly to originally thought out: Going through all the clues, marking the onePS's solved, and starting the whittling process from each.
#This makes sure that in the case of a thread terminating, there will be plenty of other threads to approach the unsolved clue from every connection, as in a ~50 clue puzzle it can be expected that there are 
#well over 10 onePS's

#it looks like it works, I just found a bug in my code, basically it can get into another loop when it can't solve something by reverse whittling, so it reverse whittles its last connection.
#if the clue is already solved, it doesn't trigger the loop avoidance because its calling reverse whittle from whittle. An easy fix is just to check if you're reverse whittling something solved, then stop.


#Now that this has basically just become the file where I write down whatever comes to mind about this program,
#it's time to come up with some tests. If it's going to be something you showcase on your profile, it needs to be good code. 
#and all good code is tested properly. Remember, it's more important to do a good job than to work hard.
#So. using unittest, you're going to test every case for every function in this program. 
# 1. block.print() - not really sure what to test for 2. block init -- what happens if it's called with weird inputs? Probably not good stuff



#stuff to do before pushing this code:
#1. test what happens if block is initialized wrong
#2. test what happens if clue is initialized wrong
#3. should probably add in command line argument for puzzle file. Don't want to have to mess with the source for each puzzle
#4. also, try and figure out if there's a better way to input the puzzle, because right now it's brutal. The thing is, dealing
#with images is hard, and not necessarily in the scope of this project. For now, just tell the user what they did wrong


#Non-test stuff to write:
#1. Add in command line arg for puzzle file
#2. SD Readme detailing how to format puzzle file, what assumptions were made, etc
#3. File IO isn't the only thing you have to do responsibly
#	--for a bunch of things, make sure the program exits gracefully, and tells the user what's wrong

#Tests to write:
#1. if run without command line arg for puzzle file, what do I want to happen? What happens?
#	--this is testing the main program execution
#2. if a clue is formatted incorrectly, what happens? 
#	--this is testing readIn
#2a. There's probably going to be a bunch of variations on this, but the place to deal with it is going to be where I cast the data types
#	
#3. now that I've given the user control over ID's, what if two clues have the same ID?
#	--this seems like a more sophisticated test
#4. What if the connection I'm looking for doesn't exist?
#	--this is testing findSecondaryConnectionIndex
#5. What happens if there's a 13+ letter clue?
#	--I just need to account for this in readIn
#6. Is there a case where the solver fails to solve a solvable puzzle?
#	--I don't think so, I think my solve function is pretty comprehensive, it will eventually whittle or solve every clue
#7. what if solve is called before readIn?
#	--I just need to check for this, maybe the simplest way is to add a bool in puzzle
#8. what if whittle is called on an unsolved clue?
#	--Same thing, just need to check in the beginning
#9. what if the connected clue I'm looking for doesn't exist?
#	--this is testing __findConnectedClue
#10. Just while we're being thorough, I should test all the print functions