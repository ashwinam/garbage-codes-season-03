"""
2. Simple Statistics: 
        Write functions to calculate basic statistics for a list of numbers:
            (i) calculate_average(numbers): This function should take a list of numbers as input and return their average (sum of all numbers divided by the number of numbers).
            (ii) find_minimum(numbers): This function should take a list of numbers as input and return the smallest number in the list.
            (iii) find_maximum(numbers): This function should take a list of numbers as input and return the largest number in the list.

The main program should ask the user to enter a list of numbers (separated by commas or spaces) and then call the functions to calculate and display the average, minimum, and maximum values.
"""


def calculate_average(numbers: list):
    return sum(numbers) / len(numbers)


def find_minimum(numbers: list):
    return min(numbers)


def find_maximum(numbers: list):
    return max(numbers)


if __name__ == "__main__":
    print("Enter the comma seperated values: ")
    usr_input = list(map(lambda num: int(num), input().split(",")))
    print(
        f'The Average is {calculate_average(usr_input)}, Minimum is {find_minimum(usr_input)} and maximum is {find_maximum(usr_input)}')
