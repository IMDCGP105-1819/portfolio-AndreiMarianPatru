# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    temp=list(secret_word)
    x=[x for x in letters_guessed if x  in secret_word  ]
    if x==temp:
        return True
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    word=[]
    temp=list(secret_word)
    for x in secret_word:
        if x in letters_guessed:
            word.append(x)
        else:
            word.append("_ ")
    final=''.join(word)
    return final



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    all=list(string.ascii_lowercase)
    available=[available for available in all if available not in letters_guessed]
    return ''.join(available)



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed=[]
    guesses=6
    warnings=3
    length=len(secret_word)

    print("Welcome to the game Hangman")
    print("I am thinking of a word that is ",length," letters long")

    while True:
        if guesses==0:
            print("You lost, the word was ",secret_word)
            break
        if letters_guessed==list(secret_word):
            print("you won!")
            score=guesses*len(secret_word)
            print("Your score is",score)
            break
        print("You have ",guesses," guesses left.")
        print("available letters: ",get_available_letters(letters_guessed))
        print("Enter your guess:")
        a=input()
        if a not in list(string.ascii_letters ):
            print("This is not a valid input")
            warnings-=1
            print("Now you have ",warnings,' left, at 3 warnings you will lose a guess')
            if warnings==0:
                guesses-=1
                warnings=3
            print("Let's try one more time!")
            continue
        else:
            if a in string.ascii_uppercase:
                a=a.lower()

            if a in letters_guessed:
                print("You already tried that guess")
                warnings-=1
                print("Now you have ",warnings,' warnings left, at 0 warnings you will lose a guess')
                if warnings==0:
                    guesses-=1
                    warnings=3
                print("Let's try one more time!")
                continue
            letters_guessed.append(a)



        if a in secret_word:
            print("Good guess:",get_guessed_word(secret_word, letters_guessed))
            continue
        else:
            print("Oops! That letter is not in word: ",get_guessed_word(secret_word, letters_guessed))
            guesses-=1
            continue

    secret_word = choose_word(wordlist)
    hangman(secret_word)
