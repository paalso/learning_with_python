##4. http://openbookproject.net/thinkcs/python/english3e/functions.html

##4. Draw this pretty pattern:

import turtle
import math

def make_window(colr, ttle):
    """
      Set up the window with the given background color and title.
      Returns the new window.
    """
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w


def make_turtle(colr, sz):
    """
      Set up a turtle with the given color and pensize.
      Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t


def draw_poly(t, n, side):
    """Make a turtle t draw a regular polygon"""
    for i in range(n):
        t.forward(side)
        t.left(360 / n)


def draw_square(t, side):
    """Make a turtle t draw a square"""
    for i in range(4):
        t.forward(side)
        t.left(90)


## ----- Main -----------------------------------------------------

wn = make_window("lightgreen", "Drawing a pretty pattern")
tortilla = make_turtle("blue", 3)


square_side = 200
shift = (2 ** 0.5) * square_side * math.sin(9 * math.pi / 180)
for i in range(5):
    draw_square(tortilla, square_side)
    tortilla.right(2 * 18)
    tortilla.penup()
    tortilla.forward(shift)
    tortilla.left(3 * 18)
    tortilla.pendown()

wn.mainloop()