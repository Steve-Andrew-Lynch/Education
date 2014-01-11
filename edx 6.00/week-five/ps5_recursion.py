# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
    if aStr == "":
        return aStr
    else:
        return aStr[-1] + reverseString(aStr[:-1])

#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if len(x) == 0:
        return True
    else:
        if x[0] in word:
            return x_ian(x[1:], word[word.find(x[0]):])
        else:
            return False

#
# Problem 5: Typewriter
#

def insertNewlines(text, lineLength):
    """
        Given text and a desired line length, wrap the text as a typewriter would.
        Insert a newline character ("\n") after each word that reaches or exceeds
        the desired line length.
        
        text: a string containing the text to wrap.
        line_length: the number of characters to include on a line before wrapping
        the next word.
        returns: a string, with newline characters inserted appropriately.
        """
    lineList = []
    result = ''
    def insertNewlinesRec(text, lineLength):
        lineList
        if len(text) < lineLength or " " not in text or text == '':
            lineList.append(text)
            return lineList
        else:
            if text[0] == ' ':
                text.replace(' ', '', 0)
                lineList.append(text[:text.find(' ', lineLength-1) +1])
                return insertNewlinesRec(text[text.find(' ', lineLength-1) + 1:], lineLength)
            else:
                lineList.append(text[:text.find(' ', lineLength-1) +1])
                return insertNewlinesRec(text[(text.find(' ', lineLength-1) + 1):], lineLength)
    
    
    
    insertNewlinesRec(text, lineLength)
    return "\n".join(lineList)
    

