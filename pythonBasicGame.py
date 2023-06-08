import random as r

"""
def play():
    user = input(" 'r' for rock , 'p' for paper , 's' for scissors  ")
    computer = r.choice(["r", "p", "s"])

    if user == computer:
        return "its a tie"

    if is_win(user, computer):
        return "you won!"

    return "you lost"


def is_win(player, opponent):

    if (
        (player == "r" and opponent == "s")
        or (player == "s" and opponent == "p")
        or (player == "p" and opponent == "r")
    ):
        return True


print(play())

"""


def play():
    user = input(" 'r' for rock , 'p' for paper , 's' for scissors , 'q' for quit  ")
    computer = r.choice(["r", "p", "s"])
    if user == "q":
        return

    if user == computer:
        return "its a tie"

    while is_win(user, computer):
        return "you won!"

    return "you lost"


def is_win(player, opponent):
    if (
        (player == "r" and opponent == "s")
        or (player == "s" and opponent == "p")
        or (player == "p" and opponent == "r")
    ):
        return True
    else:
        return False


while True:
    print(play())
