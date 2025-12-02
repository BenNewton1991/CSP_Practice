import random 

#Complete the game below
#Ensure player has option to play game again. 

options = ['rock', 'paper', 'scissors']

def interface(name):
    print('welcome ' + name + ' to rock paper scissors')
    print('you will play vs a computer')
    player_choice = input('type rock paper or scissors\n')

    while (player_choice != 'rock' and player_choice != 'paper' and player_choice != 'scissors'):
        player_choice = input('type rock paper or scissors\n')
    
    computer_choice = random.choice(options)

    if (player_choice == 'paper' and computer_choice == 'scissors'):
        print('player wins!')
    else: 
        print('no winner!')

name = input('please enter your name\n')

interface(name)