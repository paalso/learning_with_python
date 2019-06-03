##4. http://openbookproject.net/thinkcs/python/english3e/functions.html

##Write a void (non-fruitful) function to draw a square. Use it in a program to draw
##the image shown below. Assume each side is 20 units.

import turtle

def init_turtle(t, x, y, color, width):
    """Set initial position of t"""
    t.penup()
    t.setpos(x, y)
    t.color(color)
    t.width(width)
    t.pendown()


def draw_square(t, sz):
    """Make turtle t draw a square of sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()        # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Drawing of some squares")

tortilla = turtle.Turtle()
init_turtle(tortilla, -100, 0, "red", 3)

squares_number = 5
step = 30

for i in range(squares_number):
    draw_square(tortilla, step)
    tortilla.penup()
    tortilla.forward(2 * step)
    tortilla.pendown()


wn.mainloop()