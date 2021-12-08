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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
outgoingText = texts[0][0]
incomingText = texts[0][1]
timeofText = texts[0][2]

callingNumber = calls[-1][0]
receivingNumber = calls[-1][1]
timeofCall = calls[-1][2]
duration = calls[-1][3]

print("First record of texts, {} texts {} at time {}".format(outgoingText,incomingText,timeofText))
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(callingNumber,receivingNumber,timeofCall,duration))