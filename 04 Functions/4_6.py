##4. http://openbookproject.net/thinkcs/python/english3e/functions.html

##6. Write a void function draw_equitriangle(t, sz) which calls draw_poly from
## the previous question to have its turtle draw a equilateral triangle.

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


def draw_equitriangle(t, sz):
    draw_poly(t, 3, sz)

## ----- Main -----------------------------------------------------

wn = make_window("lightgreen", "Drawing a pretty pattern")
tortilla = make_turtle("blue", 2)


size = 150
draw_equitriangle(tortilla, size)

wn.mainloop()