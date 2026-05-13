
import random

# List of choices
choices = ["rock", "paper", "scissors"]

print("=== Rock Paper Scissors Game ===")

while True:
    # User input
    user = input("Enter rock, paper, or scissors: ").lower()

    if user not in choices:
        print("Invalid choice! Please try again.\n")
        continue

    # Computer choice
    computer = random.choice(choices)

    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}\n")

    # Game logic
    if user == computer:
        print("It's a tie!")
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")

    # Play again option
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break

    print()
