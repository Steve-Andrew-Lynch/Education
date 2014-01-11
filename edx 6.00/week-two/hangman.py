def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 8
    lettersGuessed = []
    isGuessed = False

    print "Welcome to the game Hangman!"
    print "I am thinking of a word that is", len(secretWord), "letters long"
    print "------------"
    while guesses > 0:
        availableLetters = getAvailableLetters(lettersGuessed)
        word = getGuessedWord(secretWord, lettersGuessed)

        print "You have", guesses, "guesses left"
        print "Available Letters:", availableLetters
        
        guess = raw_input('Please guess a letter: ')
        guess = guess.lower()


        if guess in availableLetters:
            lettersGuessed += guess
            if guess in secretWord:
                word = getGuessedWord(secretWord, lettersGuessed)
                print "Good guess: ", word
                isGuessed = isWordGuessed(secretWord, lettersGuessed)

            else:
                print "Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed)
                guesses -= 1
            lettersGuessed.append(guess)


        else:
            print "Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed)

        print "------------"
        
        if isGuessed ==  True:
            print "Congratulations! You won!"
            break
                
    if isGuessed == False:
        print "Sorry, you ran out of guesses. The word was ", secretWord


