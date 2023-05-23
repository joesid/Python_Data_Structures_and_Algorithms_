#Quiz

#  A Write isLeapYear(year)
#  B write stub daysInMonth(year, month) that always returns 30
#  c modify daysInMonth(year, month) to be correct except for leap years
#  D modify daysInMonth(year,)to account for leap years
#  E modify nextDay(year, month, day) to use daysInMonth(year, month)
#  F test isLeapYear(year)
#  G test daysInMonth(year, month) except for leap years
#  H test daysInMonth(year, month) including leap years
#  I test nextDay(year, month, day) using stub daysInMonth
#  J test daysBetweenDates(...) for simple cases
#  K test daysBetweenDates(...) for all test cases 

#BEICIAFK

def isLeapYear(year):
    boolval = False
    if year % 4 == 0:
        print("True")
    else:
        print("False")
    return boolval

isLeapYear(2020)


def daysInMonth(year, month):
    if month == 4 or  6 or 9 or 11:
        return 30
    elif month == 2:
        return 28
    else:
        return 31

def dayInMonth_ly(year,month):
    if month == 2 and isLeapYear(year):
        return 29
    else:
        return daysInMonth(year,month)

def nextDay(year, month, day):

    if day < 30:
        return year, month, day+1
    elif day == 30 and month < 12:
        day = 1
        return year, month+1, day
    elif day == 30 and month == 12:
        day = 1 
        month = 1
        return year+1, month, day 
    





