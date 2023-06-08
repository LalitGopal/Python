print("THE QUIZ GAME :)")


def quiz():
    count = 0
    print("lets start")
    a1 = input("your first question : What does CPU stands for? ").lower()
    if a1 == "central processing unit":
        print("🤩 yes that's the correct answer ")
        count += 1
    else:
        print("no that's the wrong answer")

    a2 = input("your secound question : In which year, python was launched? ").lower()
    if a2 == "1991":
        print("🤩 yes that's the correct answer ")
        count += 1
    else:
        print("no that's the wrong answer")

    a3 = input("your third question : HTML stands for? ").lower()
    if a3 == "hyper text markup language":
        print("🤩 yes that's the correct answer ")
        count += 1
    else:
        print("no that's the wrong answer")

    a4 = input("your fourth question : JavaScript was launched in? ").lower()
    if a4 == "1995":
        print("🤩 yes that's the correct answer ")
        count += 1
    else:
        print("no that's the wrong answer")

    a5 = input("your fifth question : What? ").lower()
    if a5 == "central processing unit":
        print("🤩 yes that's the correct answer ")
        count += 1
    else:
        print("no that's the wrong answer")

    if count == 5:
        print("wow 😍 you got a 5/5 !  ")
        print("thank you for playing")

    else:
        print("you have got", count, "out of 5!")
        print("thank you for playing")


def ask():
    ask = input("do you want to play the game?  ").lower()

    if ask == "yes":
        quiz()
    elif ask == "s":
        quiz()
    elif ask == "no":
        print("ok bye")
    elif ask == "No":
        print("ok bye")
    else:
        print("invalid syntax!")
        ask()


ask()
