'''
Exercise 9.8. Here’s another Car Talk Puzzler:
“I was driving on the highway the other day and I happened to notice
my odometer. Like most odometers, it shows six digits, in whole miles only.
So, if my car had 300,000 miles, for example, I’d see 3-0-0-0-0-0.
“Now, what I saw that day was very interesting. I noticed that the last 4
digits were palindromic. One mile later, the last 5 numbers were palindromic.
One mile after that, the middle 4 out of 6 numbers were palindromic. And
you ready for this? One mile later, all 6 were palindromic!
The question is, what was on the odometer when I first looked?”
'''

def is_palindrome(s):
    return s == s[::-1]


required_values = []
for i in range(100000, 1000000):
    if      is_palindrome(str(i)[2:]) \
        and is_palindrome(str(i + 1)[1:]) \
        and is_palindrome(str(i + 2)[1:5]) \
        and is_palindrome(str(i + 3)):
        required_values.append(i)

for i in required_values:
    print(i, i + 1, i + 2, i + 3)
