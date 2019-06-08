##4. http://openbookproject.net/thinkcs/python/english3e/functions.html

##9. Write a void function to draw a star, where the length of each
##side is 100 units. (Hint: You should turn the turtle by 144 degrees at each point.)

import turtle

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

def draw_star(t, sz):
    """Make a turtle t draw a five-pointed star"""
    for i in range(5):
        t.forward(sz)
        t.right(144)

## ----- Main -----------------------------------------------------

wn = make_window("lightgreen", "Drawing a star")
tortilla = make_turtle("blue", 2)

size = 150
tortilla.right(72)
draw_star(tortilla, size)

wn.mainloop()