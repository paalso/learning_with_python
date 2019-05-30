##http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html

##13. Create a turtle, and assign it to a variable. When you ask for its type, what do you get?

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

for i in range(12):
    tess = turtle.Turtle()
    tess.speed(9)
    tess.shape("turtle")
    tess.width(3)
    tess.color("blue")

    angle = i * 30
    tess.left(angle)

    tess.penup()
    size = 120
    tess.forward(size)

    tess.penup()

    size = 12
    tess.pendown()
    tess.forward(size)

    size = 20
    tess.penup()
    tess.forward(size)

    tess.stamp()

tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

##13. Create a turtle, and assign it to a variable. When you ask for its type, what do you get?
print(type(tess))


wn.mainloop()
