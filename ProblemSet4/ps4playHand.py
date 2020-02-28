# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:01:13 2020

@author: palar
"""
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    ht=hand.copy()
    w=""
   # print(wordList)
    if word=='':
        return False
    for i in word:
     #   print(i)
        if i in hand and ht.get(i)>=1:
            w+=i
            ht[i]=ht.get(i) -1
    #print("credo",w)
    if w==word and  w in wordList:
        return True
    else:
        return False

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    pl={}
    htep=hand.copy()
    for x in word:
        pl[x]= pl.get(x,0)+1
 #   print("word in dict",pl)
 #   print("hand ",hand)
    for i in pl:
        if i in htep:
#            print("encontre",i)
            htep[i]=hand.get(i) - pl.get(i)
    return htep
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    suma=0
    for i in word:
#        print(i)
        if i in SCRABBLE_LETTER_VALUES:
            #print(i,"in sc lt vl")
            ans=SCRABBLE_LETTER_VALUES.get(i)
            suma+=ans
           # print(i,"worht",ans)
    suma=suma*len(word)
    if n==len(word):
        suma+=50
    return suma
WORDLIST_FILENAME = "words.txt"
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE (download ps4a.py to see)
    total=0
    pts=0
    th=hand.copy()
    while True:
        tmp=list(th.values())
        if sum(tmp)==0:
            print('Run out of letters. Total score:',total,"points.")
            break
        print("Current Hand:",end=" ")
        displayHand(th)
        a = input('Enter word, or a "." to indicate that you are finished: ')
        if a=='.':
            print('Goodbye! Total score:',total,"points.")
            break
        else:
#            print(isValidWord(a,th,wordList))
            if isValidWord(a,th,wordList):
                pts=getWordScore(a,n)
                th=updateHand(th,a)
                total+=pts
                print('"'+str(a)+'" earned',pts,'points. Total:',total) 
            else:
                print('Invalid word, please try again.')
                

wordList = loadWords()
#print(wordList)
#print(playHand({'a': 1, 'b': 1, 'o': 1, 'r': 1}, wordList, 4))
#print(playHand({'a': 1, 'z': 1},wordList,2))
print(playHand({'a': 1, 'c': 1, 'd': 1, 'e': 3, 'k': 1, 'q': 1, 't': 1, 'x': 1},wordList,10))