import datetime

birthyear = 1994
currentyear = datetime.datetime.now().year #Declaration for getting year 
count = 0
num_years = 0
total_days = 0



#Dictionary containg calendar Months are keys and the Value are "No of Days"
calendar = {"JAN": 31, "FEB": 28, "MAR":31, "APR":30, "MAY":31, "JUNE": 30, "JULY":31, "AUG":31, "SEP":30, "Oct":31, "NOV":30, "DEC":31, "error": 'error' }




#Collect User Inputs
month = input("please enter your month; ").upper()

birthyear = int(input("please enter your birthyear: "))

day = int(input("Day of your birth "))



# Function to check Leap Year
def chk_leap(year):
    print(year)
    if year % 4 == 0:
        return True
    else:
        return False
    

#Function to check how many days in a month
def chk_days(day, month, birthyear):
    val = calendar.get(month, "error")
    if chk_leap(birthyear) is True and month == "FEB":
        val = 29
        return val
    else:
        return val 



#leapyear_b = chk_leap(birthyear)
#leapyear_c = chk_leap(currentyear)


#Count How many Leap years are between BirthYear and the Current Year
def count_leap(birthyear,currentyear):
    count = 0
    for year in range (birthyear,currentyear,1):
        if year % 4 == 0:
           count +=1
    return count


def Days_in_Month(month, year):
    ### this code is designed to calcute the number of days in am month ###
    if month in calendar:
        day = calendar.get(month, "error")
        if month == "FEB" and chk_leap(year) is True:
            day +=1
            return day
        elif month == "FEB":
            day = 28
            return day
        else:
            return day

    # for days in calendar.values():
    #     if days != "error":
    #         total_days += days
    #     else:
    #         print("Error")

def Calculate_DayRem(day_input, month, year):
    ### Calculate the days remaining in a given month from the current date
    month_days = Days_in_Month(month, year)
    days_left = month_days - day_input
    return days_left
  







#debug console 
#print(type(day))

print("month value {}: ".format(month))
print("Days in month: {}".format(Days_in_Month(month, currentyear)))
print("Days remaining in the month choosen {}: ".format(Calculate_DayRem(day, month, currentyear)))