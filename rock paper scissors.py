import random

options = ("rock", "paper", "scissors")

while True:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")


    if player == computer:
        print("It's a Tie!")
    elif player == "rock" and computer == "scissors":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "scissors" and computer == "paper":
        print("You Win!")
    else:
        print("You lose!")


    play_again = input("Play Again? (yes/no): ").lower()
    if not play_again == "yes":
        break

print("Thanks for playing!")




