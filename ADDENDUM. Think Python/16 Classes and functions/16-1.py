'''
Exercise 16.1. Write a function called mul_time that takes a Time object and
a number and returns a new Time object that contains the product of
the original Time and the number.
Then use mul_time to write a function that takes a Time object that represents
the finishing time in a race, and a number that represents the distance,
and returns a Time object that represents the average pace (time per mile).
'''

class Time:
    '''Represents the time of day.
    attributes: hours, minutes, seconds
    '''
    def __init__(self, hrs=0, mins=0, secs=0):
        ''' Creates a new MyTime object initialized to hrs, mins, secs.
           The values of mins and secs may be outside the range 0-59,
           but the resulting MyTime object will be normalized.
        '''
        totalsecs = round(60 * (60 * hrs + mins) + secs)
        self.hours = totalsecs // 3600
        self.minutes = (totalsecs // 60) % 60
        self.seconds = totalsecs % 60


    def __str__(self, hrs=0, mins=0, secs=0):
        return '{:>02}:{:>02}:{:>02}' \
            .format(self.hours, self.minutes, self.seconds)


    def add_time(self, time):
        return Time(self.hours + time.hours,
                    self.minutes + time.minutes,
                    self.seconds + time.seconds)

    def mul_time(self, number):
        return Time(self.hours * number,
                    self.minutes * number,
                    self.seconds * number)


def average_pace(distance, time):
    '''
        Returns a Time object that represents the average pace (time per mile).
        Input:  number that represents the distance in miles,
                Time object that represents the finishing time in a race
    '''
    try:
        return time.mul_time(1 / distance)
    except ZeroDivisionError:
        return 0


t = Time(0,35,56)
m = 5.02
print(average_pace(m, t))
print(average_pace(0, t))
