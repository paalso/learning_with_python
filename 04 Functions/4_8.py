##4. http://openbookproject.net/thinkcs/python/english3e/functions.html

##8. Write a function area_of_circle(r) which returns
## the area of a circle of radius r.

import math

def area_of_circle(r):
    return math.pi * r * r

## ----- Main -----------------------------------------------------

r = int(input("Intput radius:"))
print("the area of a circle of radius", r, "is",area_of_circle(r))