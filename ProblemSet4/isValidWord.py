SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
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
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

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
            print(i,"worht",ans)
    suma=suma*len(word)
    if n==len(word):
        suma+=50
    return suma

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
    print("credo",w)
    if w==word and  w in wordList:
        return True
    else:
        return False

#
# Problem #4: Playing a hand
print(isValidWord('chayote', {'a': 1, 'c': 1, 'd': 1, 'e': 3, 'k': 1, 'q': 1, 't': 1, 'x': 1},loadWords()))    
#print(isValidWord('hammer', {'m': 2, 'r': 1, 'a': 1, 'e': 1, 'h': 1},loadWords()))