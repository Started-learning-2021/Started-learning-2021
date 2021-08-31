#Rock, paper, scissors game
import random
import math
from Objects import Magic_stick

def rockpaperscissors():
    user = input("Rock, paper or scissors?: ").lower()
    computer = random.choice(['rock', 'paper', 'scissors'])

    if user == computer:
        return (0, user, computer)

    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)

def is_win(player, opponent):
    # return true is the player beats the opponent
    # winning conditions
    if (player == 'rock' and opponent == 'scissors') or (player == 'scissors' and opponent == 'paper') or (player == 'paper' and opponent == 'rock'):
        return True
    return False

def play_best_of(n):
    # play against the computer until someone wins best of n games
    # to win, you must win ceil(n/2) 
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = rockpaperscissors()
        # tie
        if result == 0:
            print('It is a tie. You and the opponent have both chosen {}. \n'.format(user))
        # you win
        elif result == 1:
            player_wins += 1
            print('You chose {} and the opponent chose {}. You won!\n'.format(user, computer))
        else:
            computer_wins += 1
            print('You chose {} and the opponent chose {}. You lost :(\n'.format(user, computer))

    if player_wins > computer_wins:
        print("You have won the best of {} games and won the magical stick! You're a champ :D".format(n))
        Magic_stick()
    else:
        print("Unfortunately, your opponent has won the best of {} games. You will need to find a magical stick elsewhere!".format(n))

if __name__ == '__main__':
    play_best_of(3) # 2