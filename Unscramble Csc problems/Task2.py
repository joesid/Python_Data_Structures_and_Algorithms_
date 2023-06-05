"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


cal_l = []
num = 0

for entry in calls:
    cal_l.append(int(entry[3]))
    num +=1
cal_l.sort()

highVal = num - 1

#print(cal_l)
large = cal_l[highVal]
 
for entry1 in calls:
    if int(entry1[3]) == large:
        print(entry1)
        print("{} spent the longest time, {} seconds, on the phone during Septemeber 2016.".format(entry1[0], entry1[3]))


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

