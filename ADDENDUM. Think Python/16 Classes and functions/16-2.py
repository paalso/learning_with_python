'''
Exercise 16.2.
1. Use the datetime module to write a program that gets the current date and
prints the day of the week.
2. Write a program that takes a birthday as input and prints the user’s age and
the number of days, hours, minutes and seconds until their next birthday.
3. For two people born on different days, there is a day when one is twice as
old as the other. That’s their Double Day. Write a program that takes two birth
dates and computes their Double Day.
4. For a little more challenge, write the more general version that computes
the day when one person is n times older than the other.
'''
import datetime


def current_day():
    '''
    Returns the current date
    '''
    import datetime
    return datetime.date.today(), datetime.date.weekday(datetime.date.today())


def current_weekday():
    '''
    Returns the day of the week
    '''
    import datetime
    int_to_weekday = ['Mon', 'Tue', 'Wed', "Thu", 'Fri', 'Sat', 'Sun']
    return int_to_weekday[datetime.date.weekday(datetime.date.today())]


def last_birthday(birthday, _now = datetime.datetime.now()):
    import datetime
    this_year_birthday = birthday.replace(year=_now.year)
    if this_year_birthday <= _now:
        return this_year_birthday
    return this_year_birthday.replace(year=_now.year-1)


def last_birthday_date(birthday):
    return last_birthday(birthday).date()


def next_birthday(birthday):
    _now = datetime.datetime.now()
    return last_birthday(birthday, _now.replace(year=_now.year+1))


def until_next_birthday(birthday):
    next_birthday_moment = next_birthday(birthday)
    _now = datetime.datetime.now()
    return next_birthday_moment - _now


def age(birthday):
    '''
    Takes a birthday date
    Returns the user’s age in years
    '''
    return last_birthday(birthday).year - birthday.year


def n_times_older_day(birthday1, birthday2, n=2):
    if birthday1 == birthday2:
        return
    if birthday1 < birthday2:
        smaller, older = birthday1, birthday2
    else:
        smaller, older = birthday2, birthday1

    delta = older - smaller
    return older + delta / (n - 1)


#16.2.2
##birthday = datetime.datetime(1974, 12, 16)
##birthday = datetime.datetime(2006, 6, 5)
##print('Last birthday:',last_birthday(birthday))
##print('Next birthday:',next_birthday(birthday))
##print('Time left until next birthday:',until_next_birthday(birthday))

#16.2.3-4
birthday1 = datetime.datetime(2010, 3, 1)
birthday2 = datetime.datetime(2006, 6, 5)
double_day = n_times_older_day(birthday1, birthday2)
print(double_day)
print(double_day - birthday1)
print(double_day - birthday2)
