##http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html

##7. A drunk pirate makes a random turn and then takes 100 steps forward,
##makes another random turn, takes another 100 steps, turns another random amount, etc.
##A social science student records the angle of each turn before the next 100 steps are taken.
##Her experimental data is [160, -43, 270, -97, -43, 200, -940, 17, -86].
##(Positive angles are counter-clockwise.) Use a turtle to draw the path taken by our drunk friend.

##8. Enhance your program above to also tell us what the drunk pirate’s heading is
##after he has finished stumbling around. (Assume he begins at heading 0).

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.width(3)
tess.color("black")

angles_list = [160, -43, 270, -97, -43, 200, -940, 17, -86]

current_angle = 0
for angle in angles_list:
    tess.forward(100)
    tess.left(angle)
    current_angle += angle

current_angle %= 360
print("The pirate is heading", current_angle,"degrees")

wn.mainloop()