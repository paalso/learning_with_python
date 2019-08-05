## Chapter 10. Event-Driven Programming
## http://openbookproject.net/thinkcs/python/english3e/events.html

## Exercise 1
## ===========
# Add some new key bindings to the first sample program:
# Pressing keys R, G or B should change tess’ color to Red, Green or Blue.
# Pressing keys + or - should increase or decrease the width of tess’ pen.
# Ensure that the pen size stays between 1 and 20 (inclusive).
# Handle some other keys to change some attributes of tess, or attributes of the
# window, or to give her new behaviour that can be controlled from the keyboard.


import turtle

def make_screen(width, height, title, bgcol = "lightgreen"):
    turtle.setup(width, height)      # Determine the window size
    wn = turtle.Screen()        # Get a reference to the window
    wn.title(title)             # Change the window title
    wn.bgcolor(bgcol)           # Set the background color
    return wn


def make_turtle(color, pensize, shape, x = 0, y = 0):
    t = turtle.Turtle()
    t.color(color)
    t.pensize(pensize)
    t.shape(shape)
    return t


# The next four functions are our "event handlers".
def h1():
   tess.forward(30)


def h2():
   tess.left(45)


def h3():
   tess.right(45)


def h4():
    wn.bye()                # Close down the turtle window


def set_red_color():        # change tess’ color to Red
    tess.color("red")


def set_blue_color():       # change tess’ color to Blue
    tess.color("blue")


def set_green_color():      # change tess’ color to Green
    tess.color("green")


def inc_pen():              # increase tess’ pen size
    current_size = tess.pensize()
    if current_size < 20:
        tess.pensize(current_size + 1)


def dec_pen():              # decrease tess’ pen size
    current_size = tess.pensize()
    if current_size > 1:
        tess.pensize(current_size - 1)


wn = make_screen(500, 400, "Handling keypresses!")
tess = make_turtle("purple", 3, "circle")



# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(set_red_color, "R")
wn.onkey(set_green_color, "G")
wn.onkey(set_blue_color, "B")
wn.onkey(inc_pen, "+")
wn.onkey(dec_pen, "-")

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()