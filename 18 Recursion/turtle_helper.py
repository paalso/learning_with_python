import turtle
import math

def move(turtle, x, y):
    """
      Set up position of the given turtle
    """
    turtle.penup()
##    turtle.goto(x, y)
    turtle.setx(x)
    turtle.sety(y)
    turtle.pendown()


def make_window(color, title):
    """
      Set up the window with the given background color and title.
      Returns the new window.
    """
    w = turtle.Screen()
    w.bgcolor(color)
    w.title(title)
    return w


def make_turtle(color, size, x = 0, y = 0, shape='turtle'):
    """
      Set up a turtle with the given color and pensize.
      Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(color)
    t.pensize(size)
    t.shape(shape)
    move(t, x, y)
    return t

def draw_polygon(turtle, angles, side, start_angle):
##    turtle.left(180 - start_angle)
    turtle.setheading(180 - start_angle)
    for i in range(angles):
        turtle.forward(side)
        turtle.left(360 / angles)

def draw_circle(turtle, radius, start_angle):
    ANGLES = 70

    side = 2 * radius * math.sin(math.radians(360 / (2 * ANGLES)))
    draw_polygon(turtle, ANGLES, side, start_angle)
