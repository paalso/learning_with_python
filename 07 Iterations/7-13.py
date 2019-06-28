##http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html

## Exercise 13
## Many interesting shapes can be drawn by the turtle by giving a list of pairs
## like we did above, where the first item of the pair is the angle to turn,
## and the second item is the distance to move forward. Set up a list of pairs
## so that the turtle draws a house with a cross through the centre, as show
## here. This should be done without going over any of the lines / edges more
## than once, and without lifting your pen.

import turtle, math

def make_window(colr, title):
    """
      Set up the window with the given background color and title.
      Returns the new window.
    """
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(title)
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

def draw_route(turtle, route, scale = 1):
    for (angle, dist) in route:
        turtle.right(angle)
        turtle.forward(dist * scale)


wn = make_window("lightgreen", "Drawing a star")
tortilla = make_turtle("red", 2)

sqr2 = math.sqrt(2)
side = 100
route = [(-135, side * sqr2), (-135, side), (-90, side), \
        (-90, side), (-45, side / sqr2), (-90, side / sqr2), \
        (-135, side), (135, side * sqr2) ]
draw_route(tortilla, route)

wn.mainloop()