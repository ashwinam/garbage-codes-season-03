"""
2. **Student Grade Organizer:**

This program utilizes lists and tuples to store and organize student grades.

- Ask the user for the number of students in the class.
- Create a list to store tuples for each student. Each tuple should contain the student's name and a list of their grades for different subjects.
- Use a loop to iterate through the number of students:
    - Get the student's name as input.
    - Create a list to store the student's grades for different subjects (obtained through another loop and user input).
    - Combine the student's name and grade list into a tuple and append it to the main student list.
- After collecting all student data, you can display the information in various ways:
    - Print the entire list of student tuples.
    - Use loops to access specific student data (e.g., print a particular student's name and grades).
    - Calculate and display average grades for each student or the entire class (using loops and conditional statements).

"""

student_list = []

user_input = int(input("How many student in a class: "))

for i in range(user_input):
    student_name = input("Whats the student name?: ")
    student_grades = input(
        "Add grades(use a space for multiple grades): ").split(" ")
    student_list.append((student_name, student_grades))

search_student = input("Student name to be search: ")

for row in student_list:
    if search_student in row:
        print("student Name", row[0])
        print("Student grade", ", ".join(row[1]))
