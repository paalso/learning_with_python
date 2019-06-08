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


def draw_cross(t, side, angle):
    """Make a turtle t draw a cross"""
    t.pendown()
    t.left(angle)
    for i in range(2):
        t.forward(side)
        t.left(180)
        t.forward(2 * side)
        t.left(180)
        t.forward(side)
        t.left(90)

    t.left(180)


def draw_inclined_square(t, side, angle):
    """Make a turtle t draw a square"""
    t.right(135 - angle)
    t.penup()
    t.forward(side / (2 ** 0.5))
    t.left(135)
    t.pendown()

    draw_square(t, side)

    t.left(45)
    t.penup()
    t.forward(side / (2 ** 0.5))
    t.right(45)
    t.penup()


def draw_inclined_grid(t, side, angle):
    draw_cross(t, side, angle)
    draw_inclined_square(t, 2 * side, 0)



## ----- Main -----------------------------------------------------

wn = make_window("lightgreen", "Drawing a pretty pattern")
tortilla = make_turtle("blue", 3)


for i in range(5):
    tortilla.left(18)
    draw_inclined_grid(tortilla, 200, 0)

wn.mainloop()