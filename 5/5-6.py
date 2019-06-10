##5. Conditionals
##http://openbookproject.net/thinkcs/python/english3e/conditionals.html

# 6. Write a function which is given an exam mark, and it returns
##a string — the grade for that mark — according to this scheme:..


def get_grade(mark):
    if mark >= 75:
        return "First"
    if mark >= 70:
        return "Upper Second"
    if mark >= 60:
        return "Second"
    if mark >= 50:
        return "Third"
    if mark >= 45:
        return "F1 Supp"
    if mark >= 40:
        return "F2"
    return "F3"


## -------------------------------------------------------------------------

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for mark in xs:
    print("Mark:", mark, ", grade:", get_grade(mark))