import random


def play():
    user_choice = input(
        "Please put 'p' for paper, 'r' for rock, and 's' for scissors: \n")
    computer_input = random.choice(['r', 'p', 's'])

    if computer_input == 'r':
        computer_choice = 'Rock'
    if computer_input == 'p':
        computer_choice = 'Paper'
    if computer_input == 's':
        computer_choice = 'Scissors'

    if user_choice == computer_input:
        return 'Tie'

    if is_win(user_choice, computer_input):
        return f'You win, Computer choose {computer_choice}!'

    return f'You lost. Because computer choose {computer_choice}!'


#r>s, s>p, p>r

def is_win(player, computer):
    if (player == 'r' and computer == 's') or \
            (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        return True


print(play())
