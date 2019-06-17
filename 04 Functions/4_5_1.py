##4. http://openbookproject.net/thinkcs/python/english3e/functions.html

##5. The two spirals in this picture differ only by the turn angle. Draw both.

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


## ----- Main -----------------------------------------------------

wn = make_window("lightgreen", "Drawing a spiral")
tortilla = make_turtle("blue", 2)

side = 5
increase = 3
angle = 90

tortilla.right(angle)
tortilla.forward(side)

for i in range(100):
    side += increase
    tortilla.right(angle)
    tortilla.forward(side)


wn.mainloop()