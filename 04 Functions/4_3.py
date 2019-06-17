##4. http://openbookproject.net/thinkcs/python/english3e/functions.html

##Write a void function draw_poly(t, n, sz) which makes a turtle draw a regular
##polygon. When called with draw_poly(tess, 8, 50), it will draw a shape like this:

import turtle

def init_turtle(t, x, y, color, width):
    """Set initial position of t"""
    t.penup()
    t.setpos(x, y)
    t.color(color)
    t.width(width)
    t.pendown()


def draw_poly(t, n, side):
    """Make a turtle t draw a regular polygon"""
    for i in range(n):
        t.forward(side)
        t.left(360 / n)


wn = turtle.Screen()        # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Drawing of some nested squares")

tortilla = turtle.Turtle()
init_turtle(tortilla, 0, 0, "red", 3)

n = int(input("Input number of angles of the polygon to draw: "))
side = 50
draw_poly(tortilla, n, side)

wn.mainloop()