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
            
secretWord="y"
letterGuessed=['y','e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed(secretWord,letterGuessed))