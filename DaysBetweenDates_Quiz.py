#Quiz
import unittest
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
    if year % 4 == 0:
        return True
    else:
        return False
    

def daysInMonth(month):
    if month == 2:
        return 28
    elif month == 4 or month == 6:
        return 30
    elif month == 9 or month == 11:
        return 30
    else:
        return 31

def dayInMonth_ly(year,month):
    if month == 2 and isLeapYear(year):
        return 29
    elif isLeapYear(year) == False:
        return daysInMonth(month)

def nextDay(year, month, day):

    if day < dayInMonth_ly(year, month):
        return year, month, day+1
    elif day == dayInMonth_ly(year,month) and month < 12:
        day = 1
        return year, month+1, day
    elif day == 31 and month == 12:
        day = 1 
        month = 1
        return year+1, month, day 
    
def daysleft(year, month, day):
    ### Find the number of days between two months###
    dayleft = dayInMonth_ly(year, month) - day
    return dayleft


print(daysleft(2, 2020, 28))



        



print(nextDay(2020,2,28))

#print(dayInMonth_ly(2021,2))



#print(daysInMonth(10))