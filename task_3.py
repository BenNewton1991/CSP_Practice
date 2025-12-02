import random 


images = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Guess the letter
#Study the game
#Consider: how does the game make use of selction, list, procedure, parameter, iteration, input, output
#EXTENSION: If you feel capable: refactor the game from guess the letter in to hangman [guess the word]

easy = ['a', 't', 's']
medium = ['p', 'o', 't']
hard = ['x', 'c', 'y']


def interface():
    game = input('easy, medium, or hard letters?\n')

    letter = ''

    lives = 5

    if (game == 'easy'):
        letter = choose_letter_list(easy)
    if (game == 'medium'):
        letter = choose_letter_list(medium)
    if (game == 'hard'):
        letter = choose_letter_list(hard)

    while lives > 0:
        guess = input('guess a letter\n')

        if guess == letter:
            print('you win!')
            break
        else:
            lives -= 1
            progress_death(lives)    

        

def progress_death(lives):
    index = len(images) - lives - 1
    if index < len(images):
        print(images[index])


def choose_letter_list(words):
    return random.choice(words)

interface()


