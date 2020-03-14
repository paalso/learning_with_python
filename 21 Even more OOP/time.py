# Chapter 21. Even more OOP
# http://openbookproject.net/thinkcs/python/english3e/even_more_oop.html

class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """ Create a MyTime object initialized to hrs, mins, secs """
        totalsecs = hrs * 3600 + mins * 60 + secs
        self.hours = totalsecs // 3600        # Split in h, m, s
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __str__(self):
        return '{:02}:{:02}:{:02}'.format(self.hours, self.minutes, self.seconds)

    def __eq__(self, time2):
        return self.to_seconds() == time2.to_seconds()

    def add_time(self, t):
        return MyTime(0, 0, self.to_seconds() + t.to_seconds())

    def __add__(self, other):
        return self.add_time(other)

    def sub_time(self, t):
        return MyTime(0, 0, self.to_seconds() - t.to_seconds())

    def __sub__(self, other):
        return self.sub_time(other)

    def after(self, time2):
        """ Return True if I am strictly greater than time2 """
        return self.to_seconds() > time2.to_seconds()

    def __gt__(self, time2):
        """
        Exercise 3
        ===========
        Turn the above function into a method in the MyTime class.
        if t1.after(t2): ...
        we can use the more convenient
        if t1 > t2: ...
        return self.to_seconds() > time2.to_seconds()
        """
        return self.after(time2)

    def before(self, time2):
        """ Return True if I am strictly greater than time2 """
        return self.to_seconds() < time2.to_seconds()

    def __lt__(self, time2):
        """
        Turn the above function into a method in the MyTime class.
        if t1.after(t2): ...
        we can use the more convenient
        if t1 < t2: ...
        """
        return self.before(time2)

    def between(self, time1, time2):
        """
        Exercises 1, 2
        ===========
        Write a Boolean function between that takes two MyTime objects,
        t1 and t2, as arguments, and returns True if the invoking object falls
        between the two times. Assume t1 <= t2, and make the test closed at
        the lower bound and open at the upper bound, i.e. return True
        if t1 <= obj < t2.
        Turn the above function into a method in the MyTime class.
        """
        return time1.to_seconds() <= self.to_seconds() < time2.to_seconds()

    def increment(self, secs=0):
        """
        Exercises 4
        Rewrite increment as a method that uses our “Aha” insight.
        """
        new_secs = self.to_seconds() + secs
        self.hours = new_secs // 3600        # Split in h, m, s
        leftoversecs = new_secs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60
        return self


def test_suite():
    """
    Create some test cases for the increment method. Consider specifically
    the case where the number of seconds to add to the time is negative.
    Fix up increment so that it handles this case if it does not do so already.
    (You may assume that you will never subtract more seconds than are in
    the time object.)
    """

    from testtools import test

    print("\n'increment()' testing...")
    t = MyTime(1, 15, 42)
    test(t.increment(0) == t)
    test(t.increment(10) == MyTime(1, 15, 52))

    t = MyTime(1, 15, 42)
    test(t.increment(18) == MyTime(1, 16, 00))

    t = MyTime(1, 15, 42)
    test(t.increment(3600) == MyTime(2, 15, 42))
    test(t.increment(3672) == MyTime(3, 16, 54))
    test(t.increment(-7200) == MyTime(1, 16, 54))
    test(t.increment(-4614) == MyTime())


def main():
    test_suite()


if __name__ == '__main__':
    main()
