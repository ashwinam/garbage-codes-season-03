"""
1. Area Calculator: 
    Write three functions:
        (i) calculate_square_area(side_length): This function should take the side length of a square as input and return its area (side_length * side_length).
        (ii) calculate_rectangle_area(length, width): This function should take the length and width of a rectangle as input and return its area (length * width).
        (iii) calculate_triangle_area(base, height): This function should take the base and height of a triangle as input and return its area (0.5 * base * height).

The main part of your program should then ask the user which shape they want to calculate the area for (square, rectangle, or triangle) and prompt them for the necessary dimensions. Finally, call the appropriate function based on the user's choice and display the calculated area.
"""


def calculate_square_area(side_length):
    '''Add side_length for calculating the area of a square: '''
    return side_length * side_length


def calculate_rectangle_area(length, width):
    '''Add length and width for calculating the area of a Rectangle(Add space in between values): '''
    return length * width


def calculate_triangle_area(base, height):
    '''Add base and height for calculating the area of a Triangle(Add space in between values): '''
    return 0.5 * base * height


func_dictionary = {
    1: calculate_square_area,
    2: calculate_rectangle_area,
    3: calculate_triangle_area
}


if __name__ == "__main__":
    print('''Which one you want to calculate the area
    Following is the options:
    1. Square
    2. Rectangle
    3. Triangle''')

    usr_input = int(input("Type the number: "))
    func = func_dictionary[usr_input]
    func_argument_inputs = input(func_dictionary[usr_input].__doc__).split(" ")
    if func.__name__ != 'calculate_square_area':
        arg1 = int(func_argument_inputs[0])
        arg2 = int(func_argument_inputs[1])
        print(f'The {" ".join(func.__name__.split("_"))} is {func(arg1, arg2)}.')
    else:
        arg = int(func_argument_inputs[0])
        print(f'The {" ".join(func.__name__.split("_"))} is {func(arg)}.')
