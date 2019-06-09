##5. Conditionals
##http://openbookproject.net/thinkcs/python/english3e/conditionals.html

# 1. Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday.
# Write a function which is given the day number, and it returns the day name (a string).

def day_name (n):
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
        return "Monday"
    elif n == 2:
        return "Saturday"
    else:
        return "error"


n = int(input("The week's day number:"))
print(day_name(n))