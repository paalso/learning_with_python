## Chapter 10. Event-Driven Programming
## http://openbookproject.net/thinkcs/python/english3e/events.html

## Exercise 3
## ===========
# In an earlier chapter we saw two turtle methods, hideturtle and showturtle
# that can hide or show a turtle. This suggests that we could take a different
# approach to the traffic lights program. Add to your program above as follows:
# draw a second housing for another set of traffic lights. Create three
# separate turtles to represent each of the green, orange and red lights,
# and position them appropriately within your new housing. As your state
# changes occur, just make one of the three turtles visible at any time.
# Once you’ve made the changes, sit back and ponder some deep thoughts:
# you’ve now got two different ways to use turtles to simulate
# the traffic lights, and both seem to work. Is one approach somehow
# preferable to the other? Which one more closely resembles reality —
# i.e. the traffic lights in your town?

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

orange_turtle = make_turtle("orange", 1, "circle", 3, \
                            green_turtle.xcor(), green_turtle.ycor() + 70)
orange_turtle.hideturtle()

red_turtle = make_turtle("red", 1, "circle", 3, \
                            green_turtle.xcor(), green_turtle.ycor() + 140)
red_turtle.hideturtle()

time = 1500
state_1 = 0
state_2 = 0


def state_machine_1():
    global state_1
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
    if state_2 == 0:
        green_turtle.hideturtle()
        orange_turtle.showturtle()
        state_2 = 1
        wn.ontimer(state_machine_2, time)
    elif state_2 == 1:
        orange_turtle.hideturtle()
        red_turtle.showturtle()
        state_2 = 2
        wn.ontimer(state_machine_2, int(time / 3))
    else:
        red_turtle.hideturtle()
        green_turtle.showturtle()
        state_2 = 0
        wn.ontimer(state_machine_2, time)


state_machine_1()
state_machine_2()

wn.mainloop()




##def state_machine_2():
##    global state_2
##    if state_2 == 0:
##        green_turtle.color("darkgrey")
##        orange_turtle.color("orange")
##        state_2 = 1
##        wn.ontimer(state_machine_2, time)
##    elif state_2 == 1:
##        orange_turtle.color("darkgrey")
##        red_turtle.color("red")
##        state_2 = 2
##        wn.ontimer(state_machine_2, time)
##    else:
##        red_turtle.color("darkgrey")
##        green_turtle.color("green")
##        state_2 = 0
##        wn.ontimer(state_machine_2, time)