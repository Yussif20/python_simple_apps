import random

def get_user_choice():
    """
    Prompts the user to enter their choice and validates the input.

    Returns:
        str: The valid choice entered by the user.
    """
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        if user_choice in choices:
            return user_choice
        print("Invalid choice. Please try again.")

def get_computer_choice():
    """
    Randomly selects the computer's choice.

    Returns:
        str: The computer's choice.
    """
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """
    Determines the winner of the game based on the user's and computer's choices.

    Args:
        user_choice (str): The user's choice.
        computer_choice (str): The computer's choice.

    Returns:
        str: The result of the game (win, lose, or tie).
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """
    Plays a round of Rock-Paper-Scissors.
    """
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
