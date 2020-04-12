# Exercise 3.1. Write a function named right_justify that takes a string
# named s as a parameter and prints the string with enough leading spaces so
# that the last letter of the string is in column 70 of the display.


def right_justify(string, width=70):
    size = len(string)
    if size >= width:
        return string
    return ' ' * (width - size) + string


s = 'monty'
print(right_justify(s))
