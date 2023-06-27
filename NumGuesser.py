import random
import os
def ConsoleClear():
    os.system('cls' if os.name == 'nt' else 'clear')
ConsoleClear()

print("Welcome to Guess the Number")

playGame = int(input("1. Play\n2. Exit\n"))
ConsoleClear()
while playGame != 2:


    guessCorrect = False
    compChoice = random.randint(1, 100)
    counter = 0

    userGuess = int(input("Guess a number: "))
    ConsoleClear()
    counter += 1

    while guessCorrect == False:
        if userGuess == compChoice:
            guessCorrect == True
            break
        elif userGuess > compChoice:
            print("Too high")
            counter += 1
        else:
            print("Too low")
            counter += 1
        
        userGuess = int(input("Guess a number: "))
        ConsoleClear()

    print(f"It took you {counter} guesses to guess {userGuess}")
    print(f"The correct number was {compChoice}")

    playGame = int(input("1. Play\n2. Exit\n"))
    ConsoleClear()
