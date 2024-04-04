"""
1. Guessing Game: Write a program that plays a guessing game with the user. The program should think of a random number between 1 and 100 (or any other chosen range). The user should then guess the number. Use a while loop to let the user keep guessing until they guess the correct number. If the guess is too high or too low, provide hints to the user.
"""

import random

comp_guessed_number = random.randint(1, 100)  # random number from 1 to 100

print('computer guessed number: ', comp_guessed_number)

while True:
    usr_input = int(input('Guess Your Number: '))
    if usr_input > comp_guessed_number:
        print('You guess is hight please think lowest number.')
    if usr_input < comp_guessed_number:
        print('Please go for a higher number.')
    if usr_input == comp_guessed_number:
        print('You Won, Congratulations!')
        break
