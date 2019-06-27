##http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html

## Exercise 11
## Revisit the drunk pirate problem from the exercises in chapter 3.
## This time, the drunk pirate makes a turn, and then takes some steps forward,
## and repeats this. Our social science student now records pairs of data:
## the angle of each turn, and the number of steps taken after the turn.
## Her experimental data is [(160, 20), (-43, 10), (270, 8), (-43, 12)].
## Use a turtle to draw the path taken by our drunk friend.

import turtle
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

route = [(160, 20), (-43, 10), (270, 8), (-43, 12)]
##route = [(90, 10), (90, 10), (90, 10), (90, 10)]
draw_route(tortilla, route, 5)

wn.mainloop()