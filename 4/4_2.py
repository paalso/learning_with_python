##4. http://openbookproject.net/thinkcs/python/english3e/functions.html

##Write a program to draw this. Assume the innermost square is 20 units per side,
##and each successive square is 20 units bigger, per side, than the one inside it.

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
wn.title("Drawing of some nested squares")

tortilla = turtle.Turtle()
init_turtle(tortilla, 0, 0, "red", 3)

squares_number = 5
size = 20
step = 20

for i in range(squares_number):
    draw_square(tortilla, size)
    tortilla.penup()
    tortilla.setpos(tortilla.xcor() - step / 2, tortilla.ycor() - step / 2)
    tortilla.pendown()
    size += step

wn.mainloop()