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
def move_forward():
   tess.forward(30)


def turn_left():
   tess.left(45)


def turn_right():
   tess.right(45)


def close():
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


def inc_screen():           # increase screen size
    w, h = wn.screensize()
    wn.screensize(int(w * 1.2), int(h * 1.2))
    print(f"Current screensize: {w}, {h}")


def dec_screen():           # decrease screen size
    w, h = wn.screensize()
    wn.screensize(int(w / 1.2), int(h / 1.2))
    print(f"Current screensize: {w}, {h}")


def change_screen_color():
    bgcol = input("New background color:")
    wn.bgcolor(bgcol)


def print_info():
    print(f"""
    Current turtle state:
        x, y = {round(tess.xcor())}, {round(tess.ycor())}
        heading = {tess.heading()}
        color: {tess.color()}
        pensize = {tess.pensize()}
    """)

wn = make_screen(500, 400, "Handling keypresses!")
tess = make_turtle("purple", 3, "circle")



# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(move_forward, "Up")
wn.onkey(turn_left, "Left")
wn.onkey(turn_right, "Right")
wn.onkey(set_red_color, "r")
wn.onkey(set_green_color, "g")
wn.onkey(set_blue_color, "b")
wn.onkey(close, "q")
wn.onkey(inc_pen, "+")
wn.onkey(dec_pen, "-")
wn.onkey(inc_screen, "Prior")
wn.onkey(dec_screen, "Next")
wn.onkey(change_screen_color, "BackSpace")
wn.onkey(print_info, "i")


# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()