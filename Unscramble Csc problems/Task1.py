"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re
import os 

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

my_texts = []
n = 0
for i in texts:
        my_texts.append(i[0])
        my_texts.append(i[1])

print(len(my_texts))

my_calls = []
for i in calls:
     my_calls.append(i[0])
     my_calls.append(i[1])

print(len(my_calls))

num = 0


fixed_pattern = r'\(\d{2,}\)\d{8,9}'

mobile_pattern = r'[789]\d{4} \d{5}'
telemarketer_pattern = r'140\d{7}'

fix = 0
mobile = 0
tele = 0

my_fix=[] 
my_mobile=[]
my_tele=[]

for i in my_calls:
   
    if re.search(fixed_pattern,i):
        fix +=1
        my_fix.append(i)
        #print(i)
    elif re.search(mobile_pattern, i):
         mobile+=1
         my_mobile.append(i)
        
    elif re.search(telemarketer_pattern, i):
         tele+=1
         my_tele.append(i)
    
# for i in my_calls:
#      print(i)

        

total = fix + mobile + tele
print(total)

unique_mobile = list(set(my_mobile))
unique_mobile.sort()

unique_fix = list(set(my_fix))
unique_fix.sort()

unique_tele = list(set(my_tele))
unique_tele.sort()

with open("fixed_mobile.txt", "w") as file:
     file.truncate()
     for item in unique_fix:
          file.write(str(item) + '\n')

print("there are {} of fixed phone lines".format(len(unique_fix)))
print("there are {} of mobile phone lines".format(len(unique_mobile)))
print("there are {} of telemarketer phone lines".format(len(unique_tele)))

    
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
