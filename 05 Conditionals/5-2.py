##5. Conditionals
##http://openbookproject.net/thinkcs/python/english3e/conditionals.html

# 2. You go on a wonderful holiday (perhaps to jail, if you don’t like happy
##exercises) leaving on day number 3 (a Wednesday). You return home after
##137 sleeps. Write a general version of the program which asks for the starting
##day number, and the length of your stay, and it will tell you the name
##of day of the week you will return on.

def weekday_name (n):
    if n == 0:
        return "Sunday"
    elif n == 1:
        return "Monday"
    elif n == 2:
        return "Tuesday"
    elif n == 3:
        return "Wednesday"
    elif n == 4:
        return "Thursday"
    elif n == 5:
        return "Friday"
    elif n == 2:
        return "Saturday"
    else:
        return "error"


def weekday_number (name):
    days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    return days.index(name.lower())


def weekday_after(day_name, days_to_pass):
    return weekday_name((weekday_number(day_name) + days_to_pass) % 7)


## -------------------------------------------------------------------------
leave_day = input("The day to leave:")
days_away = int(input("Days to stay away:"))
print("The day to return:", weekday_after(leave_day, days_away))