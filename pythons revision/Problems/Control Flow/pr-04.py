"""
4.Average Grade Calculator: Write a program that calculates the average grade for a student. The program should ask the user for the number of grades. Use a for loop to iterate and get the individual grades as input.  Store them in a list. Then, calculate the average using a loop or built-in functions and display the result. You can extend this by using if statements to assign letter grades based on the average score.
"""

print("Enter Your grades in a space sepeated values")
grades = input()
list_of_grades = list(map(lambda ele: int(ele), grades.split(" ")))


average = sum(list_of_grades) / len(list_of_grades)

print('The average is ', average)
