'''
Exercise 5.1. The time module provides a function, also named time, that
returns the current Greenwich Mean Time in “the epoch”, which is an arbitrary
time used as a reference point. On UNIX systems, the epoch is 1 January 1970.
Write a script that reads the current time and converts it to a time of day in
hours, minutes, and seconds, plus the number of days since the epoch.
'''


def daytime():
    import time
    daytime_seconds = time.time() % (3600 * 24)
    hours = int(daytime_seconds // 3600)
    minutes = int((daytime_seconds - hours * 3600) // 60)
    seconds = round(daytime_seconds % 60)
    return hours, minutes, seconds


print(daytime())
