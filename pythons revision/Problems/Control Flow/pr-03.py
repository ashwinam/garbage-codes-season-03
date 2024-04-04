"""
3.FizzBuzz:  This classic program iterates through a range of numbers (typically 1 to 100). Use a for loop to iterate through the numbers. Print the number itself for normal cases. However, if the number is divisible by 3, print "Fizz" instead. If it's divisible by 5, print "Buzz". If it's divisible by both 3 and 5, print "FizzBuzz".
"""

for i in range(1, 100):
    output = ''
    if i % 3 == 0:
        output += 'Fizz'
    if i % 5 == 0:
        output += 'Buzz'
    print(output or i)
