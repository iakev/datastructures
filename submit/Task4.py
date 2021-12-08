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

#Make a list of numbers called,recieved texts or sent texts.
telemarketers = []
others = []
for i in range(len(texts)):
    others.append(texts[i][0])
    others.append(texts[i][1])

for i in range(len(calls)):
    others.append(calls[i][1])

for i in range(len(calls)):
    if calls[i][0] not in others:
        telemarketers.append(calls[i][0])

tele = set(telemarketers)
tele1 = list(tele)
tele1.sort()

print("These numbers could be telemarketers: ")
for i in range(len(tele1)):
  print(tele1[i])