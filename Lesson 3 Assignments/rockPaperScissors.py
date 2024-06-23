import random

# Get user input for their choice
user_choice = input("Enter your choice (rock, paper, or scissors): ")

# Generate the computer's choice
computer_choice = random.choice(["rock", "paper", "scissors"])

# Determine the winner
if user_choice.lower() == computer_choice:
    print("It's a tie!")
elif (user_choice.lower() == "rock" and computer_choice == "scissors") or \
     (user_choice.lower() == "paper" and computer_choice == "rock") or \
     (user_choice.lower() == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("The computer wins!")