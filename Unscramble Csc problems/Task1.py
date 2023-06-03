"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
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
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
