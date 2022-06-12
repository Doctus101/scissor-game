import random
import math

def play():
    user = input("what is your preferred choice?, 'r' for Rock 'p' for Paper 's' for Scissors\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return (0, user, computer)

    if is_win(user, computer):
            return (1, user, computer)
            
    return (-1, user, computer)

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

def play_best_of(n):
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    print(wins_necessary)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()

        if result == 0:
            print('it is a tie.you and the computer have both chosen {}. \n'.format(user))

        elif result == 1:
            player_wins += 1
            print('you have chose {} and the computer chose {}. you won!\n'.format(user, computer))
        else:
            computer_wins += 1
            print('you have chose {} and the computer chose {}. you lost!\n'.format(user, computer))
        print('\n')

    if player_wins > computer_wins:
        print('you have won! what a champ'.format(n))
    else:
        print('unfortunately, the computer has won.Better luck next time!'.format(n))


if __name__=='__main__':
    play_best_of(1)
    
    

