'''
Exercise 15.2. Write a function called draw_rect that takes a Turtle object and
a Rectangle and uses the Turtle to draw the Rectangle. See Chapter 4 for
examples using Turtle objects. Write a function called draw_circle that takes
a Turtle and a Circle and draws the Circle.
'''
from figures import Circle, Rectangle, Point
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


def draw_rect(t, rectangle):
    tortilla.penup()
    start_point = rectangle.get_topleft()
    tortilla.setpos(start_point.get_x(), start_point.get_y())
    tortilla.pendown()
    tortilla.setheading(0)
    for i in range(2):
        tortilla.forward(rectangle.get_width())
        tortilla.right(90)
        tortilla.forward(rectangle.get_height())
        tortilla.right(90)


def draw_circle(t, rectangle):
    t.penup()
    start_point = rectangle.get_topleft()
    t.setpos(start_point.get_x(), start_point.get_y())
    t.pendown()
    t.setheading(0)
    for i in range(2):
        t.forward(rectangle.get_width())
        t.right(90)
        t.forward(rectangle.get_height())
        t.right(90)


def draw_circle(t, circle):
    t.penup()
    start_point = circle.get_center()
    radius = circle.get_radius()
    tortilla.setpos(start_point.get_x(), start_point.get_y() - radius)
    t.pendown()
    tortilla.circle(radius)


wn = make_window("lightgreen", "Drawing a star")
tortilla = make_turtle("red", 2)
rect = Rectangle(Point(120, -65), 50, 150)
circle = Circle(Point(0, 0), 180)

draw_rect(tortilla, rect)
draw_circle(tortilla, circle)
wn.mainloop()