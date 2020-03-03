# Chapter 19. Exceptions
# http://openbookproject.net/thinkcs/python/english3e/exceptions.html

# Exercise 1
# ===========
# Write a function named readposint that uses the input dialog to prompt
# the user for a positive integer and then checks the input to confirm that it
# meets the requirements. It should be able to handle inputs that cannot be
# converted to int, as well as negative ints, and edge cases (e.g. when
# the user closes the dialog, or does not enter anything at all.)


def readposint():
    ERR_MSG = "Couldn't get a positive integer number"
    try:
        number = int(input('Input a positive integer: '))
        if number > 0:
            return number
        if number <= 0:
            print(ERR_MSG)
            return None
    except:
        print(ERR_MSG)


def main():
    n = readposint()
    print(n)


if __name__ == '__main__':
    main()
