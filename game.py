from utils import get_computer_choice, determine_winner

def main():
    """Runs the Rock, Paper, Scissors game."""
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        return

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
