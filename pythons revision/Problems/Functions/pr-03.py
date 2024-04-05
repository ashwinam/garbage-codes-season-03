"""
3. Rock, Paper, Scissors Game: Design functions to represent the game logic:

(i) generate_computer_choice(): This function should randomly generate the computer's choice ("rock", "paper", or "scissors").
(ii) play_round(user_choice, computer_choice): This function should take the user's choice and computer's choice as input and determine the winner based on the classic Rock-Paper-Scissors rules. It should return a message indicating the winner (user, computer, or tie).

The main program should prompt the user for their choice, call the relevant functions, and display the round result. You can extend this by playing multiple rounds and keeping track of the score.
"""


def generate_computer_choice():
    import random
    return random.choice(["rock", "paper", "scissor"])


def play_round(usr_choice, computer_choice):
    if usr_choice == 'rock' and computer_choice == 'scissor':
        print("User Wins")
    elif usr_choice == 'scissor' and computer_choice == 'paper':
        print('User Wins')
    elif usr_choice == 'paper' and computer_choice == 'rock':
        print("User Wins")
    elif computer_choice == 'rock' and usr_choice == 'scissor':
        print('Computer Wins')
    elif computer_choice == 'scissor' and usr_choice == 'paper':
        print('Computer Wins')
    elif computer_choice == 'paper' and usr_choice == 'rock':
        print("Computer Wins")
    else:
        print("Its a Tie.")


if __name__ == "__main__":

    usr_input = input("""
Select from the following options:
Rock, Paper, Scissor
""").lower()
    while usr_input not in ["rock", "paper", "scissor"]:
        print("Must be select from Rock, Paper, Scissor")
        usr_input = input("""
Select from the following options:
Rock, Paper, Scissor
""").lower()
    computer_input = generate_computer_choice()
    play_round(usr_input, computer_input)
