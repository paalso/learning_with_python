# Chapter 23. Inheritance
# http://openbookproject.net/thinkcs/python/english3e/inheritance.html

# Exercise 2
# ===========
# Define a new kind of Turtle, TurtleGTX, that comes with some extra features:
# it can jump forward a given distance, and it has an odometer that keeps track
# of how far the turtle has travelled since it came off the production line.
# (The parent class has a number of synonyms like fd, forward, back, backward,
# and bk: for this exercise, just focus on putting this functionality into
# the forward method.) Think carefully about how to count the distance if
# the turtle is asked to move forward by a negative amount.
# (We would not want to buy a second-hand turtle whose odometer reading was
# faked because its previous owner drove it backwards around the block too often.
# Try this in a car near you, and see if the car’s odometer counts up or down
# when you reverse.)

# Exercise 3
# ===========
# After travelling some random distance, your turtle should break down with
# a flat tyre. After this happens, raise an exception whenever forward is
# called. Also provide a change_tyre method that can fix the flat.

import turtle, random


class DamageTyre(Exception):
    pass


class FlatTyre(Exception):
    pass


class TurtleGTX(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.total_dist = 0
        self.total_breaks = 0
        self.are_tyres_safe = True

    def odometer(self):
        return self.total_dist

    def breaks(self):
        return self.total_breaks

    def forward(self, dist):
        if not self.are_tyres_safe:
            raise Exception("You can't drive: you've got a flat tyre")
        if random.randrange(15) == 13:
            self.are_tyres_safe = False
            self.total_breaks += 1
            raise Exception("Oops, you've broken down with a flat tyre")
        turtle.Turtle.forward(self, dist)
        self.total_dist += abs(dist)

    def rand_direction(self):
        new_direction = random.randrange(181)
        if random.randrange(2):
            self.left(new_direction)
        else:
            self.right(new_direction)

    def change_tyre(self):
        self.are_tyres_safe = True


def make_window(colr, ttle):
    """
      Set up the window with the given background color and title.
      Returns the new window.
    """
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w


def make_turtle(colr, sz):
    """
      Set up a turtle with the given color and pensize.
      Returns the new turtle.
    """
    # t = turtle.Turtle()
    t = TurtleGTX()
    t.color(colr)
    t.pensize(sz)
    return t


def main():
    import keyboard
    wn = make_window("lightgreen", "Drawing a star")
    t = make_turtle("blue", 2)

    moves = 0
    breaks = 0

    while True:

        key = keyboard.read_key()
        if key == 'q':
            break
        elif key == 'c':
            t.change_tyre()
            print("You've changed a tyre and may drive on")
        else:
            t.rand_direction()
            try:
                t.forward(50)
                moves += 1
            except:
                print("Oops, you've broken down with a flat tyre, move # {}"
                    .format(moves))
                print("To change a tyre press 'c'")

    print('Your journey is finished. Moves: {}, odometer: {}, breaks: {}'
        .format(moves, t.odometer(), t.breaks()))
    wn.mainloop()


if __name__ == "__main__":
    main()
