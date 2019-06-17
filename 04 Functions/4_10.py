##4. http://openbookproject.net/thinkcs/python/english3e/functions.html

## 10. Extend your program above. Draw five stars, but between each,
##pick up the pen, move forward by 350 units, turn right by 144,
##put the pen down, and draw the next star. You’ll get something like this:

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
tortilla = make_turtle("red", 2)

tortilla.penup()
tortilla.goto(0, 200)
tortilla.pendown()

size = 100
tortilla.right(72)
for i in range(5):
    draw_star(tortilla, size)
    tortilla.penup()
    tortilla.forward(350)
    tortilla.pendown()
    tortilla.right(144)

wn.mainloop()