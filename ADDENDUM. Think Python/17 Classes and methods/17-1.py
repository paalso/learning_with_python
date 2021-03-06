'''
Exercise 17.1. Download the code from this chapter from
http://thinkpython2.com/code/Time2.py
Change the attributes of Time to be a single integer representing seconds
since midnight. Then modify the methods (and the function int_to_time) to work
with the new implementation. You should not have to modify the test code in
main. When you are done, the output should be the same as before.
'''

"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""


class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        """Initializes a time object.

        hour: int
        minute: int
        second: int or float
        """
        self.seconds = self._time_to_int(hour, minute, second)

    def get_seconds(self):
        return self.seconds

    def __str__(self):
        """Returns a string representation of the time."""
        hour, minute, second = self._int_to_time(self.seconds)
        return '%.2d:%.2d:%.2d' % (hour, minute, second)

    def print_time(self):
        """Prints a string representation of the time."""
        print(str(self))

    def is_after(self, other):
        """Returns True if t1 is after t2; false otherwise."""
        return self.seconds > other.get_seconds()

    def __add__(self, other):
        """Adds two Time objects or a Time object and a number.

        other: Time object or number of seconds
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)

    def add_time(self, other):
        """Adds two time objects."""
        assert self.is_valid() and other.is_valid()
        return Time(*self._int_to_time(self.seconds + other.get_seconds()))

    def increment(self, seconds):
        """Returns a new Time that is the sum of this time and seconds."""
        seconds += self.seconds
        return Time(*self._int_to_time(seconds))

    def is_valid(self):
        """Checks whether a Time object satisfies the invariants."""
        return self.seconds < 86400

    def _int_to_time(self, seconds):
        """Converts self.seconds (the number of seconds since midnight) to
        the tuple hour, minute, second
        seconds: int seconds since midnight.
        """
        minutes, second = divmod(seconds, 60)
        hour, minute = divmod(minutes, 60)
        return hour, minute, second

    def _time_to_int(self, hours, minutes, seconds):
        """Computes the number of seconds since midnight."""
        minutes += hours * 60
        seconds += minutes * 60
        return seconds % 86400


def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time(hour, minute, second)
    return time


def main():
    start = Time(9, 45, 00)
    start.print_time()

    end = start.increment(1337)
    #end = start.increment(1337, 460)
    end.print_time()

    print('Is end after start?')
    print(end.is_after(start))

    print('Using __str__')
    print(start, end)

    start = Time(9, 45)
    duration = Time(1, 35)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print('Example of polymorphism')
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print(total)


if __name__ == '__main__':
    main()

