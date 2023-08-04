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

send_texts = []
mobile_pattern = r'[789]\d{3,5}\s\d+'

send_texts = {row[0] for row in texts}
    
# for log in calls:
#     if re.match(mobile_pattern, log[0]):
#         mobile_callers.append(log[0])
        
mobile_callers = {row[0] for row in calls if re.match(mobile_pattern, row[0])}

matched_no  = []

def intersect(a, b):
    intersect_set = set()
    for element in a:
        if element in b:
            intersect_set.add(element)
    return intersect_set

matched_no = intersect(send_texts, mobile_callers)

list_tele = list(set(matched_no))

print("These numbers could be telemarketers: ")

for number in sorted(list_tele):
    print(number)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

