import random


def play():
    user = input(
        "Choose your weapon! \n 'r' for Rock, 'p' for Paper, 's' for Scissors \n"
    )
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print(computer)
        return 'It\'s a Tie'


# R beats S, S beats P, P beats R
    if is_win(user, computer):
      print(computer)  
      return 'You has won'

    print(computer)
    return 'You has lost'


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's'and opponent== 'p') \
      or (player == 'p' and opponent == 'r'):
        return True


print(play())
