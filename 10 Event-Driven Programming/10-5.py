## Chapter 10. Event-Driven Programming
## http://openbookproject.net/thinkcs/python/english3e/events.html

## Exercise 5
## ===========
# ...But your new client needs a change. They want four states in their state
#  machine: Green, then Green and Orange together, then Orange only, and then
# Red. Additionally, they want different times spent in each state.
# The machine should spend 3 seconds in the Green state, followed by one
# second in the Green+Orange state, then one second in the Orange state,
# and then 2 seconds in the Red state. Change the logic in the state machine.

import turtle


def make_screen(width, height, title, bgcol = "lightgreen"):
    turtle.setup(width, height)      # Determine the window size
    wn = turtle.Screen()        # Get a reference to the window
    wn.title(title)             # Change the window title
    wn.bgcolor(bgcol)           # Set the background color
    return wn


def make_turtle(color, pensize, shape, shapesize = 1, x = 0, y = 0):
    t = turtle.Turtle()
    t.color(color)
    t.pensize(pensize)
    t.shape(shape)
    t.shapesize(shapesize)
    t.penup()
    t.setpos(x, y)
    t.pendown()
    return t


def draw_housing(t, x, y, color1, color2):
    t.penup()
    t.goto(x, y)
    t.color(color1, color2)
    t.pendown()
    t.begin_fill()
    t.forward(80)
    t.left(90)
    t.forward(200)
    t.circle(40, 180)
    t.forward(200)
    t.left(90)
    t.end_fill()


def transform_turtle(turtle, shape, shapesize, color):
    turtle.shape(shape)
    turtle.shapesize(shapesize)
    turtle.fillcolor(color)


wn = make_screen(600, 500, "Tess becomes a traffic light!")
tess = make_turtle("purple", 3, "arrow")

# Traffic lights № 1
draw_housing(tess, -200, -100, "purple", "darkgrey")
tess.forward(40)
tess.penup()
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
transform_turtle(tess, "circle", 3, "green")

# Traffic lights № 2
green_turtle = make_turtle("purple", 3, "arrow")
draw_housing(green_turtle, 100, -100, "purple", "darkgrey")
green_turtle.forward(40)
green_turtle.penup()
green_turtle.left(90)
green_turtle.forward(50)

transform_turtle(green_turtle, "circle", 3, "green")

orange_turtle = make_turtle("slategray", 1, "circle", 3, \
                            green_turtle.xcor(), green_turtle.ycor() + 70)

red_turtle = make_turtle("slategray", 1, "circle", 3, \
                            green_turtle.xcor(), green_turtle.ycor() + 140)

time = 1500
state_1 = 0
state_2 = 0


def state_machine_1():
    global state_1
    print(f"Traffic light # 1 state: {state_1}")
    if state_1 == 2:
        tess.forward(-140)
        tess.fillcolor("green")
        state_1 = 0
        wn.ontimer(state_machine_1, time)
    elif state_1 == 1:
        tess.forward(70)
        tess.fillcolor("red")
        state_1 = 2
        wn.ontimer(state_machine_1, time)
    else:
        tess.forward(70)
        tess.fillcolor("orange")
        state_1 = 1
        wn.ontimer(state_machine_1, int(time / 3))


def state_machine_2():
    global state_2
    print(f"Traffic light # 2 state: {state_2}")
    if state_2 == 0:
        orange_turtle.color("orange")
        state_2 = 1
        wn.ontimer(state_machine_2, time)
    elif state_2 == 1:
        green_turtle.color("slategray")
        state_2 = 2
        wn.ontimer(state_machine_2, time)
    elif state_2 == 2:
        orange_turtle.color("slategray")
        red_turtle.color("red")
        state_2 = 3
        wn.ontimer(state_machine_2, 2 * time)
    else:
        red_turtle.color("slategray")
        green_turtle.color("green")
        state_2 = 0
        wn.ontimer(state_machine_2, 3 * time)


state_machine_1()
state_machine_2()

wn.mainloop()
