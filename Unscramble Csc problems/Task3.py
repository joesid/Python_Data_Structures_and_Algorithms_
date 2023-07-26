"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


my_calls = [] #initialize list for total calls

bangalore_log = []  #initialize a list for all calls from Bangalore
bangalore_call = []  #Initialize a list for all numbers dialled from a Bangalore number
area_code_list = []
mobile_prefix = []

fixed_pattern = r'\((\d{3,5})\)'
mobile_pattern = r'[789]\d{3,5}\s\d+'


bg_pattern =r'^\(080\)'  #pattern for finding banglore Numbers
tl_pattern = r'^140' #pattern for finding tele numbers 

#find log initated from a bangalore number
for log in calls:
    if re.search(bg_pattern, log[0]):
    # if i[0].startswith('(080)'):
        bangalore_log.append(log)

#Find area codes and mobile prefixes called by bangalore number
for log in bangalore_log:
    if re.match(fixed_pattern, log[1]):
        called_no = str(log[1])
        char_to_find = ')'
        position = called_no.index(char_to_find)
        area_code = called_no[:position + 1]
        area_code_list.append(area_code)
    
    elif re.match(mobile_pattern, log[1]):
        called_no = log[1]
        area_code = called_no[:6]
        mobile_prefix.append(area_code)
    
    

sort_area_code = list(set(area_code_list))
sort_area_code.sort()
sort_mobile_prefix = list(set(mobile_prefix))
sort_mobile_prefix.sort()

print('the unique area codes called by bangalore numbers')
for i in sort_area_code:
    print(i)

print('\n')
print('the mobile prefixes of numbers called by bangalore numbers ')
for i in sort_mobile_prefix:
    print(i)

#initialize list for fixed no 2 fixed no
bg_fix_to_fix = [] 

#Sort out 'fixed to fixed' line calls into a list 
for log in bangalore_log:
    if log[1].startswith('(080)'):
        bg_fix_to_fix.append(log)

total_fix_calls = len(bangalore_log)
bg_to_bg = len(bg_fix_to_fix)

fix_only_percent = (bg_to_bg/total_fix_calls) * 100

int_percen = int(fix_only_percent)


#Part B Solution 
print(f"\n{int_percen} percent of calls from fixed lines in Bangalore are calls to other fixed lines")




"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
