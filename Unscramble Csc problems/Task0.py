"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import os

import csv
with open('./texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)



with open('./calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    print(calls)
    calls.reverse()

tex_l = []
for i in texts[0]:
    tex_l.append(i)
    
cal_l = []
for i in calls[0]:
    cal_l.append(i)


print("First record of text, {} text {} at time {}".format(tex_l[0], tex_l[1], tex_l[2]))

print("Last record of calls, {} calls {} at time {} lasting seconds".format(cal_l[0], cal_l[1], cal_l[2], cal_l[3]))
"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"

"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

