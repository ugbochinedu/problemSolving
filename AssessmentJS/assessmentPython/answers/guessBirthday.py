birthday = 15


def guessBirthday(birthday):
    guess = eval(input("What is my birthday?\n"))
    while guess != birthday:
        if guess == birthday:
            print("Correct Guess")
        else:
            print("InCorrect Guess")
        guess = eval(input("What is my birthday?\n"))

guessBirthday(birthday)
