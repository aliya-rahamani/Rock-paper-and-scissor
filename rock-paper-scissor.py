import random
import math
print("===Rock Paper Scissor===\n")

def play():
    user= input("What's your choice? 'r' for rock 'p' for paper and 's' for scissors\n")
    user=user.lower()

    computer = random.choice(['r','s','p'])

    if user == computer:
        return (0, user,computer)
    elif is_winner(user,computer):
        return (1,user,computer)

    else:
        return (-1,user,computer)

def is_winner(user,computer):
    if (user == 'r' and computer == 's') or  (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True
    return False

def play_best_of(n):
    player_wins= 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while (player_wins<wins_necessary) or (computer_wins<wins_necessary):
        result, user,computer=play()
        if result == 0:
            print('It is a tie. You and the computer have both chosen {}. \n'.format(user))
            # you win
        elif result == 1:
            player_wins += 1
            print('You chose {} and the computer chose {}. You won!\n'.format(user, computer))
        else:
            computer_wins += 1
            print('You chose {} and the computer chose {}. You lost :(\n'.format(user, computer))

    if player_wins > computer_wins:
        print('You have won the best of {} games! What a champ :D'.format(n))
    else:
        print('Unfortunately, the computer has won the best of {} games. Better luck next time!'.format(n))


if __name__ == '__main__':
    play_best_of(3)  # 2











