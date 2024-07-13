import random

while True:
    #Prompt for user to choose rock, paper or scissors
    user=input("Enter a choice (rock, paper, scissors):")

    #Computer generates a random choice
    possibleActions=["rock", "paper", "scissors"]
    computer=random.choice(possibleActions)

    print(f"You chose {user} and the computer chose {computer}")

   #Game logic and displaying result
    if user==computer:
        print(f"Both players chose {user}. It's a tie!")
    elif user=='rock':
        if computer=='paper':
            print("Paper beats rock. You loose!")
        if computer=='scissors':
            print("Rock beats scissors. You win!")
    elif user=='paper':
        if computer=='rock':
            print("Paper beats rock. You win!")
        if computer=='scissors':
            print("Scissors beats paper. You loose!")
    elif user=='scissors':
        if computer=='rock':
            print("Rock beats scissors. You loose!")
        if computer=='paper':
            print("Scissors beats paper. You win!")

    play=input("Play again?(yes/no):")
    if play.lower()!="yes":
        break
