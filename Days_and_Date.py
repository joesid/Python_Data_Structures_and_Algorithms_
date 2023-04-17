import datetime

birthyear = 1994
currentyear = datetime.datetime.now().year #Declaration for getting year 
count = 0
num_years = 0
c= 0
total_days = 0



#Dictionary containg calendar Months are keys and the Value are "No of Days"
calendar = {"JAN": 31, "FEB": 28, "MAR":31, "APR":30, "MAY":31, "JUNE": 30, "JULY":31, "AUG":31, "SEP":30, "Oct":31, "NOV":30, "DEC":31, "error": 'error' }




#Collect User Inputs
month = input("please enter your month; ").upper()

birthyear = input("please enter your birthyear: ")

day = input("Day of your birth ")



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

print(month)

#Count How many Leap years are between BirthYear and the Current Year
def count_leap(birthyear,currentyear):
    count = 0
    for year in range (birthyear,currentyear,1):
        if year % 4 == 0:
           count +=1
    return count


def Calc_d(month, birthyear, currentyear):
    if month == "FEB":
        days = 28
    elif month == "FEB" and chk_leap(birthyear):
        days = 29
 

    for days in calendar.values():
        if days != "error":
            total_days += days
        else:
            print("Error")

    print(type(total_days))
    print(type(days))



num_years = 2023 - 1994
not_leap = num_years - count



print(total_days)
print(not_leap)
print(num_years)
print(count)
