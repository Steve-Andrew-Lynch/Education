# 6.00x Problem Set 5
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    cipherBook = {}
    upperBook = {}
    lowerBook = {}
    upperLetters = []
    lowerLetters = []
    upperLetters = [e for e in string.ascii_uppercase]
    lowerLetters = [e for e in string.ascii_lowercase]

    #write a dictionary that flexibly shifts letters paired with letters

    #create a for loop that assigns a dictionary value (shifted) paired with a key based on the sequence of ascii uppercase and appends to cipherBook
    for e in string.ascii_uppercase:
        upperBook[e] = upperLetters.index(e) + shift
    upperBook.update([(k, v - 26) for (k, v) in upperBook.iteritems() if v > 25])
    upperBook.update([(k, upperLetters[v]) for (k, v) in upperBook.iteritems()])

    #create a for loop that does the same, except for ascii lowercase
    for i in string.ascii_lowercase:
        lowerBook[i] = lowerLetters.index(i) + shift
    lowerBook.update([(k, v - 26) for (k, v) in lowerBook.iteritems() if v > 25])
    lowerBook.update([(k, lowerLetters[v]) for (k, v) in lowerBook.iteritems()])

    cipherBook = upperBook.copy()
    cipherBook.update(lowerBook)
    return cipherBook

    



def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    codedText = []
    for c in text:
        if c in coder:
            codedText.append(coder[c])
        else:
            codedText.append(c)
    return "".join(codedText)






def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    return applyCoder(text, buildCoder(shift))

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    #declare an empty list textList that we're going to use for our text.
    textList = []
    textCopy = ''

    #declare bestShift initially at zero
    bestShift = 0 

    #declare a bestCounter for identified words for the best shift option so far
    bestCounter = 0

    

    #iterate through 0 to 25
    for n in range(26):

        #declare a zeroed-out counter for identified words
        counter = 0
        
        #for each iteration, apply applyCoder with the iterator
        textCopy = applyCoder(text, buildCoder(n))
        
        #split the sting into words, seperated by spaces
        textList = textCopy.split(' ')

        #for each element in textList, run isWord
        for w in textList:
                
            #if True, increment counter
            if isWord(wordList, w):
                    counter += 1

        #if counter is larger than bestCounter, set bestCounter to counter and bestShift to iterator
        if counter > bestCounter:
            bestShift = n


    #return bestShift
    return bestShift






def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    text = getStoryString()
    cipher = findBestShift(loadWords(), text)
    return applyShift(text, cipher)


#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    wordList = loadWords()
    s = applyShift('Hello, world!', 8)
    bestShift = findBestShift(wordList, s)
    assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    #    decryptStory()
