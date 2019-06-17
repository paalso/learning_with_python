##4. http://openbookproject.net/thinkcs/python/english3e/functions.html

##7. Write a fruitful function sum_to(n) that returns the sum of all integer
##numbers up to and including n. So sum_to(10) would be 1+2+3...+10
##which would return the value 55.

def sum_to(n):
    return n * (n + 1) // 2

## ----- Main -----------------------------------------------------

n = int(input("Intput an positive integer number:"))
print("1 + 2 + ... +",n,"=",sum_to(n))