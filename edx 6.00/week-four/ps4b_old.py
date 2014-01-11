from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    runningScore = 0
    
    def isValidWordComp(word, hand):
        theHand = {}
        theHand = hand.copy()
        isWordTrue = False
        # does it pass the hand test?
        for i in word:
            if i not in theHand:
                return isWordTrue
            elif theHand[i] == 0:
                return isWordTrue
            elif i in theHand > 0:
                theHand[i] -= 1
        isWordTrue = True
        return isWordTrue

    # Create a new variable to store the best word seen so far (initially None)
    bestWord = None

    # For each word in the wordList
    for word in wordList:

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWordComp(word, hand):

            # Find out how much making that word is worth
            runningScore = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if runningScore > maxScore:

                # Update your best score, and best word accordingly
                maxScore = runningScore
                bestWord = word

    # return the best word you found.
    return bestWord

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    def sortHand(hand):
        extraHand = hand.copy()
        printableHand = []
        while True:
            if sum(extraHand.itervalues()) == 0:
                printableHand.sort()
                printableHand = " ".join(printableHand)
                return printableHand
            else:
                for k, v in extraHand.iteritems():
                    if v > 0:
                        printableHand.append(k)
                        extraHand[k] = v - 1
                    else:
                        pass
    
    # Keep track of the total score
    score = 0
    compPlay = True

    # to start playing
    while True:
    
        #Game is over is computer uses all of the letters in its hand
        if calculateHandlen(hand) == 0:
            print 'Total score: ' + str(score) + ' points.'
            compPlay = False
            break
        else:
            # Display the hand
            print "Current hand: " + str(sortHand(hand))
            # Get a best word for that hand
            aBestWord = compChooseWord(hand, wordList, n)
            word = aBestWord
            #if computer returns base case of None for word choice, game over
            if word == None:
                print 'Total: ' + str(score) + ' points\n'
                compPlay = False
                break
            #else, the score is based on compChooseWord's choice
            else:
                score += getWordScore(word, n)
                print '"' + word + '" earned ' + str(getWordScore(word, n)) + ' points. Total: ' + str(score) + ' points\n'
                # Update the hand
                hand = updateHand(hand, word)

#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    #define variables you will be using (is game live, input exists, player is one of the players
    hand = {}
    fInput = ''
    while fInput != 'e':
        #while game is running
        fInput = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        fInput = str(fInput)
        
        if fInput == 'e':
            break

        #if input is new game, ask choice
        if fInput == 'n':
            while True:
                #ask if it's a computer game, a human game or computer game
                fInput = ''
                cInput = raw_input('Enter u to have yourself play, c to have the computer play: ')
                cInput = str(cInput)
                #if human, deal hand, set last hand, playHand
                if cInput == 'u':
                    hand = dealHand(HAND_SIZE)
                    lastHand = hand.copy()
                    playHand(hand.copy(), wordList, HAND_SIZE)
                    print
                    break
                #if computer, deal hand, set last hand, compPlayHand
                if cInput == 'c':
                    hand = dealHand(HAND_SIZE)
                    lastHand = hand.copy()
                    compPlayHand(hand.copy(), wordList, HAND_SIZE)
                    print
                    break
                #else
                else:
                    print 'Invalid command.'
                    print
        #if last game and a previous game happened, follow similar structure for a new game, with the last hand passed through
        if fInput == 'r':
        #if player chose last game and a previous game did not happen, print statement and continue loop
            if hand == {}:
                print 'You have not played a hand yet. Please play a new hand first!\n'
                fInput = ''
            else:
                while True:
                    #ask if it's a computer game, a human game or computer game
                    fInput = ''
                    cInput = raw_input('Enter u to have yourself play, c to have the computer play: ')
                    cInput = str(cInput)
                    #if human, playHand passing lastHand
                    if cInput == 'u':
                        playHand(lastHand, wordList, HAND_SIZE)
                        print
                        break
                    #if computer, compPlayHand passing lastHand
                    if cInput == 'c':
                        compPlayHand(lastHand, wordList, HAND_SIZE)
                        print
                        break
                    #else
                    else:
                        print 'Invalid command.'
                        print
        #if unexpected input...
        elif len(fInput) > 0 and fInput !='e':
            print 'Invalid command.'
            print
        
 


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


