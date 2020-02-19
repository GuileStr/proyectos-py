# Hangman game
#
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    size=len(secretWord)
    listSecretWord=list(secretWord)
    secretReveal=""
    for i in range(size):
        listSecretWord[i]="_ "
    for i in lettersGuessed:    
        if i in secretWord:
            for x in range(size):
                if i == secretWord[x]:
                    #print("la letra",i,"esta en ",x)
                    listSecretWord[x]=i
                    secretReveal="".join(listSecretWord)
    if secretReveal==secretWord:
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    size=len(secretWord)
    listSecretWord=list(secretWord)
    #secretReveal=""
    for i in range(size):
        listSecretWord[i]="_ "
    for i in lettersGuessed:    
        if i in secretWord:
            for x in range(size):
                if i == secretWord[x]:
                    #print("la letra",i,"esta en ",x)
                    listSecretWord[x]=i
                    #secretReveal="".join(listSecretWord)
    return "".join(listSecretWord)

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
    # FILL IN YOUR CODE HERE...
    size=len(secretWord)
    mistakes=0
    con=0
    secretReveal=getGuessedWord(secretWord,[])
    guesses=8
    gl=[]
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is ",size," letters long.")
    print("-------------")
    while guesses>0:
        if isWordGuessed(secretWord,gl):
            return print("Congratulations, you won!")
            break
#        print(guesses)
        letters=getAvailableLetters(gl)##GETAVAILABLELETTERS
        print("You have",guesses,"guesses left.")
        print("Available letters:",letters)
        gl.append(input("Please guess a letter: "))
        con+=1
        
        if gl[con-1] in letters:
           # print("Ingresaste: ",gl[con-1])
            temp=secretReveal
            secretReveal=getGuessedWord(secretWord,gl) #GETGUESSEDWORD
            if secretReveal==temp:
                guesses-=1
                mistakes+=1
                print("Oops! That letter is not in my word:",secretReveal)
            else:
                print("Good guess:",getGuessedWord(secretWord,gl))
        else:
            print("Oops! You've already guessed that letter: ",secretReveal)
        print("------------")
            
        #guesses-=1
    if secretReveal!=secretWord:
        return print("Sorry, you ran out of guesses. The word was",secretWord)

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)

#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(getAvailableLetters(lettersGuessed))    

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
secretWord= "c"#chooseWord(wordlist).lower()
print(hangman(secretWord))
