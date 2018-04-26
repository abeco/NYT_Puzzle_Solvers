This is a puzzle solver written for a NYT puzzle game called Split Decisions.

Game: The only clues in this crossword are the letter pairs provided in the grid. Each answer across and down consists of two words which share the letters to be entered into the empty squares. In the example below, the letters S, E, and W are added to complete the words SINEW and SCREW. Some of the combinations in the grid may have more than one possible answer, but only one will fit with all the crossings.

(See RealPuzzleUnsolved for what the puzzle actually looks like.)

What I did to solve it was first I marked up the puzzle and gave every clue an ID. (See InkedRealPuzzleUnsolved) Then I entered the clues into a text file in the format ID Clue-Length Block-Start-Index Block-Top-Letter-Pair Block-Bottom-Letter-Pair Connections(with format Connected-Clue-ID Connection-Index). (See RealPuzzle.txt)

Then, once I had a decent way of entering the clues, I split the English language into files based on word length (I know, not a great way to do something but this is the first iteration of this program, so I just needed something that worked) and cycled through the appropriate file for potential solutions, or words with letters in the right places. 

Then, once I had all the clues, their connections, and their potential solutions, I came up with two main functions for deciding on which potential solution was the correct one, Whittle, and ReverseWhittle. I'd start out with the first clue that was already able to be solved without using its connections (I know, this is an assumption I make in order to solve the puzzle, that there will be at least one clue that can be solved without the use of its connections) I'd then call Whittle on it, which whittles down its connections' list of potential solutions to eliminate ones that don't fit with the solved clue's answer. I'd then recursively call whittle on solved clues and reverse whittle (which gets called on an unsolved clue and whittles down its own list of potential solutions based on solved connections) until either every clue was solved or there was a piece of information that was needed that hadn't been whittled yet. In that case I'd end that thread of execution and wait for another thread to come back to it, since each call to whittle and reverse whittle explores all the connected clues. 

I plan on updating this with a django webapp in the coming weeks.

