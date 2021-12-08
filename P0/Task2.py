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

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
#make an integer list of all durations
calling = []
called = []
callsduration= []
phone_dict = {}

for i in range(len(calls)):
    calling.append(calls[i][0])
    called.append(calls[i][1])
    callsduration.append(calls[i][3])
    
    # if calling[i] in phone_dict.keys():
    #     phone_dict[calling[i]] += int(callsduration[i])
    # else:
    #     phone_dict[calling[i]] = int(callsduration[i])

    # if called[i] in phone_dict.keys():
    #      phone_dict[called[i]] += int(callsduration[i])
    # else:
    #     phone_dict[called[i]] = int(callsduration[i])

    phone_dict[calling[i]] = phone_dict.get(calling[i],0) + int(callsduration[i])
    phone_dict[called[i]] = phone_dict.get(called[i],0) + int(callsduration[i])


max_duration = max(phone_dict.values())

for key in phone_dict:
    if max_duration == phone_dict[key]:
        max_durationKey = key

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_durationKey,max_duration))
