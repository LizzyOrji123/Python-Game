import random

CHOICES = ["rock", "paper", "scissors"]

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(CHOICES)

def determine_winner(user_choice, computer_choice):
    """Determine the winner using imported logic."""
    from choices.rock import beats as rock_beats
    from choices.paper import beats as paper_beats
    from choices.scissors import beats as scissors_beats

    if user_choice == computer_choice:
        return "It's a tie!"

    if (user_choice == "rock" and rock_beats(computer_choice)) or \
       (user_choice == "paper" and paper_beats(computer_choice)) or \
       (user_choice == "scissors" and scissors_beats(computer_choice)):
        return "You win!"
    
    return "Computer wins!"
