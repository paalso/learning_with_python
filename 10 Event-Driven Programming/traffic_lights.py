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


def draw_housing():
    tess.color("purple", "darkgrey")
    tess.penup()
    tess.goto(0, -100)
    tess.pendown()
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


wn = make_screen(400, 500, "Tess becomes a traffic light!")
tess = make_turtle("purple", 3, "arrow")

draw_housing()
tess.forward(40)
tess.penup()
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

# This variable holds the current state of the machine
state = 0

def advance_state_machine():
    global state
    if state == 0:
        tess.forward(70)
        tess.fillcolor("orange")
        state = 1
    elif state == 1:
        tess.forward(70)
        tess.fillcolor("red")
        state = 2
    else:
        tess.forward(-140)
        tess.fillcolor("green")
        state = 0


# Bind the event handler to the space key.
wn.onkey(advance_state_machine, "space")

wn.listen()         # Listen for events

wn.mainloop()