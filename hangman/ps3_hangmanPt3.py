import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    letters= string.ascii_lowercase
    letterTemp=""
    for i in lettersGuessed:
        if i in letters:
            letterTemp= letters.replace(i,"")
            letters=letterTemp
    #print(letters)
    return letters

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))