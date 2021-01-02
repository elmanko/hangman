import random
import os

IMAGES = ['''
    
    +----+
    |    |
         |
         |
         |
         |
         ==========''', '''

    +----+
    |    |
    O    |
         |
         |
         |
         ==========''', '''

    +----+
    |    |
    O    |
    |    |
         |
         |
         ==========''', '''

    +----+
    |    |
    O    |
   /|    |
         |
         |
         ==========''', '''

    +----+
    |    |
    O    |
   /|\   |
         |
         |
         ==========''', '''

    +----+
    |    |
    O    |
   /|\   |
    |    |
         |
         ==========''', '''

    +----+
    |    |
    O    |
   /|\   |
    |    |
   /     |
         ==========''', '''

    +----+
    |    |
    O    |
   /|\   |
    |    |
   / \   |
         ==========''', '''

''']

WORDS = [
    'can',
    'you',
    'feel',
    'the',
    'love',
    'tonight',
    'pinche',
    'pendejo'
]

def random_word():
    idx = random.randint(0,len(WORDS) - 1)
    return WORDS[idx]

def display(hidden_word, tries):
    if tries > 0:
        os.system('clear')
        display_header()
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('\n##########################################################')


def run_game():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display(hidden_word, tries)
        current_letter = str(input('Type a Letter: '))

        letter_indexes = []
        for i in range(len(word)):
            if word[i] == current_letter:
                letter_indexes.append(i)
        if len(letter_indexes) == 0:
            tries += 1
            if tries == 7:
                display(hidden_word, tries)
                print('')
                print('Dammit, you killed the poor fuck,\nanyway, the word was: {}'.format(word))
                break
        else:
            for i in letter_indexes:
                hidden_word[i]= current_letter
            letter_indexes = []

        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('Phew!\nthat MoFo sweat it out,\nthe word was \"{}\", good job!'.format(word))
            break

def display_header():
    print('H A N G M A N\n\nGuess the word and don\'t hang the poor fuck!')

if __name__ == "__main__":
    display_header()
    run_game()

