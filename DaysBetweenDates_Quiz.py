#Quiz

#Write isLeapYear(year)
#write stub daysInMonth(year, month) that always returns 30
#modify daysInMonth(year, month) to account for leap years
#modify nextDay(year, month, day) to use daysInMonth(year, month)
#test isLeapYear(year)
#test daysInMonth(year, month) except for leap years
#test daysInMonth(year, month) including leap years
#test nextDay(year, month, day) using stub daysInMonth
#test daysBetweenDates(...) for simple cases
#test daysBetweenDates(...) for all test cases 


def isLeapYear(year):
    boolval = False
    if year % 4 == 0:
        print("True")
    else:
        print("False")
    return boolval

isLeapYear(2020)
