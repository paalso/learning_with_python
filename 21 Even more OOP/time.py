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

    def between(self, time1, time2):
        return time1.to_seconds() <= self.to_seconds() <= time2.to_seconds()


t1 = MyTime(1, 15, 42)
t2 = MyTime(3, 50, 30)
t = MyTime(2, 52, 4)
print(t.between(t1, t2))
print((t + MyTime(1,30,0)).between(t1, t2))
