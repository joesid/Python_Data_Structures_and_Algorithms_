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
    if year % 4 == 0 and (year % 100 !=0 or year % 400 == 0):
        return True
    else:
        return False
    

def daysInMonth(month):
    day = 0
    if month == 2:
        day = 28
    elif month == 4 or month == 6:
        day = 30
    elif month == 9 or month == 11:
        day = 30
    else:
        day = 31

    return day 

def dayInMonth_ly(year,month):
    if month == 2 and isLeapYear(year):
        return 29
    #elif isLeapYear(year) == False:
    #   days = int(daysInMonth(month))
    #   return days 
    else:
        days = daysInMonth(month)
        return days 

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


def daysBtwnMonth(year, month2, month1):
    """Days Between Month, count the number of dates between months"""
    total_days = 0
    month1 +=1
    for month in range(month1, month2):
        if isLeapYear(year) and month == 2:
            total_days += 29
        else:
            total_days += daysInMonth(month)

    return total_days    
    
def daysBtwnYear(year1, year2):
    """Calculate the number of Days between two given years"""
    total_days = 0
    days = 0
    year1 +=1
    
    for year in range(year1,year2):
        if isLeapYear(year):
            days += 366
        else:
            days += 365 

    total_days +=days
    return total_days

def dayRemYear(month, year):
    """Days Remaining from a given month to the end of the year """
    t_days = 0
    day = 0
    month = month + 1
    if month <= 12:
        for montht in range(month,13):
           if isLeapYear(year) and montht == 2:
               day =29
           elif montht == 2:
               day = 28
           elif montht == 4 or montht == 6 or montht == 9 or montht== 11:
               day =30
           else:
               day = 31
           t_days +=day      
        
    return t_days


def sec_yr(year, month):
    """Find the no of day in the 2nd year before the month of the 2nd day"""
    day = 0
    t_day = 0
    for mon in range(1,month):
        day = dayInMonth_ly(year, mon)
        t_day += day 
    return t_day

def dayBetweenDate(year2, month2, day2, year1, month1, day1):
    day_num = 0
    dayInMonth1 = dayInMonth_ly(year1, month1)
    dayInMonth2 = dayInMonth_ly(year2, month2)
   # add = daysBtwnMonth(year1, month2, month1)
    day_years = daysBtwnYear(year1, year2)

    if year2 == year1 and month2 == month1:
        day_num = day2 - day1
    elif year2 == year1 and month2 > month1:
        day_num = daysBtwnMonth(year1, month2, month1)+ (dayInMonth1 - day1) + (dayInMonth2 - (dayInMonth2 - day2))
    elif year2 > year1:
        day_num = day_years + (dayInMonth1 - day1) + (dayRemYear(month1, year1)) + (sec_yr(year2, month2)) + (dayInMonth2 - (dayInMonth2 - day2)) 

    return day_num


dates = daysBtwnYear(2012,2017) 
print(dates) 


def test():  

    dates = dayBetweenDate(2022,2,3,2020,1,15)
    print("day between dates value is {}".format(dates))
    
    dby = daysBtwnYear(2017,2088)

    if dby == 22567:
        print("dayBtwnYear function works correctly\n")
    else:
        print("review dayBtwnYear Function, your value was {}\n".format(dby))

    dby = dayRemYear(1,2020)

    if dby == 335:
       print("dayRemYear function works correctly\n")
    else:
        print("review dayRemYear function your value was: {}\n".format(dby))
    
    dby = sec_yr(2020,5)

    if dby == 121:
        print("sec_yr function works correctly\n")
    else:
        print("sec_yr function needs review, your value was {} instead of 121\n".format(dby))
    
    
    dby = daysBtwnMonth(2020, 7, 1)

    if dby == 151:
        print("daysBtwnMonth function works successfully\n")
    else:
        print("reviews daysBtwnMonth funtion your value was {} instead of 182\n".format(dby))

    
    #days = dayInMonth_ly(2021, 4)
    #print("Days in function leap year: {}".format(days))

    #count = daysBtwnMonth(2020, 3, 1)
    #print(count)


    #print(daysleft(2, 2020, 28))

    #print(nextDay(2020,2,28))


test()