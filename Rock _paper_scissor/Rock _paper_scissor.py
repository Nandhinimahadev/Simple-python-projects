import random
import sys

playerWins = 0
computerWins = 0

options = ["rock", "paper", "scissors"]

while True:
    playerInput = input("Play Choose Rock/Paper/Scissors or Q to quit:").lower()
    if playerInput == "q":
        break
    elif playerInput not in options:
        continue
    else:
        randomNumber = random.randint(0, 2)
        # where rock =0 ,paper =1 and scissors=2
        computerChoice = options[randomNumber]
        print(f"Computer picks {computerChoice}")

        if playerInput == "rock" and computerChoice == "scissors":
            print("You Won!!")
            playerWins += 1
        elif playerInput == "paper" and computerChoice == "rock":
            print("You won!!")
            playerWins += 1
        elif playerInput == "scissors" and computerChoice == "paper":
            print("You won!!")
        elif playerInput == computerChoice:
            print("Match Draw")
        else:
            print("You lost!!")
            computerWins += 1
print("You won", playerWins, "times")
print("The Computer won", computerWins, "times")
print("Goodbye!!")
