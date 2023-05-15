
#Following a course on Data Structure and Algorithms and this was a simple exercise assigned

# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
#check if the second date comes before the first date
   # day_b4 = False
    
   if year1 < year2:     #2nd Solution 
       return True
   if year1 == year2:
       if month1 < month2:
           return True
       if month1 == month2:
           return day1 < day2
   return False

#    if year2 > year1:    #My Answer 
#        day_b4 = True
#    elif year2 < year1:
#        day_b4 = False
#    elif year2 == year1 and month2 > month1:
#        day_b4 = True
#    elif year2 == year1 and month2 < month1:
#        day_b4 = False
#    elif (year2 == year1 and month2 == month1) and day2 > day1:
#        day_b4 = True   
#    elif (year2 == year1 and month2 == month1) and day2 < day1:
#        day_b4 = False

#    return day_b4 


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    
    isDayb4 = dateIsBefore(year1, month1, day1, year2, month2, day2)
    print(isDayb4)

    total_years = year2 - year1
    total_month = month2 - month1
    no_of_days = 0
    
    def daysleft (month, day):
        monthleft = 12 - month
        dayleft = 30 - day
        total_days = dayleft + (4 * 30)  #test code
        #total_days = dayleft + (monthleft * 30)
        return  total_days


    if year2 == year1 and month2 == month1:
        no_of_days = day2 - day1
    elif year2 == year1 and month2 > month1:
        #no_of_days = (total_month * 30) + (30 - day1) + (30 - day2)
       # no_of_days = daysleft(month1, day1) + (30 - day1) + day2
       no_of_days = daysleft(month1,day1) + day2
        
    elif year2 == year1 and month2 < month1:
        no_of_days = (total_month * 30) 
    elif year2 > year1 and month2 == month1:
        day_bet_yr = (30 * 12) * total_years
        no_of_days = (day2 - day1) + day_bet_yr
    elif year2 > year1 and month2 > month1:
        day_bet_yr = (30 * 12)*total_years
        no_of_days = ((30 * 2)*total_years) + (total_month * 30) + (30 - day1) + (30 - day2)
    # YOUR CODE HERE!
    return no_of_days

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print 
            "Test with data:", args, "failed"
        else:
            print 
            "Test case passed!"

test()

days = daysBetweenDates(2013, 1, 24, 2013, 6, 29)
print(days)


   