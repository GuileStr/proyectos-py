# Hangman game
#
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

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

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
secretWord= chooseWord(wordlist).lower()
listSecretWord=list(secretWord)
guesses=8
secretReveal=""
size=len(secretWord)
for i in range(size):
    secretReveal+="_ "
    listSecretWord[i]="_ "
letters="abcdefghijklmnopqrstuvwxyz"
print ("Choosen word",chooseWord(wordlist))
print("Welcome to the game, Hangman!")
print("I am thinking of a word that is",len(secretWord),"letters long.")
print("-------------")
newLetters=""
temp=""
while guesses>0:
    if secretReveal==secretWord:
        print("Congratulations, you won!")
        break
    print("You have ",guesses,"guesses left.")
    print("Available letters:",letters)
    gl=input("Please guess a letter: ")
    if gl in secretWord:
        ##aqui voy a poner el metodo de simon
        if gl not in letters:
            print("Oops! You've already guessed that letter:",secretReveal)    
        else:
            for i in range(size):
                if secretWord[i]==gl:
                    listSecretWord[i]=gl
            secretReveal="".join(listSecretWord)
            #print("".join(listSecretWord))#Esta si jala chido
            newLetters=letters.replace(gl,"")
            letters=newLetters
            print("Good guess:",secretReveal)
    else:
        ##Aqui voy a poner el metodo de que no esta xd
        if gl not in letters:
            print("Oops! You've already guessed that letter:",secretReveal)    
        else:
            print("Oops! That letter is not in my word:",secretReveal)
            newLetters=letters.replace(gl,"")
            letters=newLetters
            guesses-=1
    print("------------")

if secretReveal!=secretWord:
    print("Sorry, you ran out of guesses. The word was",secretWord)

#print("You have",guesses,"guesses left.")

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    

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






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
