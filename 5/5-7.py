##4. http://openbookproject.net/thinkcs/python/english3e/functions.html

## 7. Modify the turtle bar chart program so that the pen is up
##for the small gaps between each bar.

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


def make_turtle(colr, color_bg, sz):
    """
      Set up a turtle with the given color and pensize.
      Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(colr, color_bg)
    t.pensize(sz)
    return t


def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()
    t.left(90)
    t.forward(height)     # Draw up the left side
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)         # Width of bar, along the top
    t.right(90)
    t.forward(height)     # And down again!
    t.left(90)            # Put the turtle facing the way we found it.
    t.penup()
    t.forward(10)         # Leave small gap after each bar
    t.pendown()
    t.end_fill()

## ----- Main -----------------------------------------------------

wn = make_window("lightgreen", "Drawing a star")
tess = make_turtle("blue", "red", 2)

xs = [48, 117, 200, 240, 160, 260, 220]

for v in xs:              # Assume xs and tess are ready
    draw_bar(tess, v)



wn.mainloop()