## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os

# Let us print the files in the directory in which you are running this script
print (os.listdir("."))
print (os.listdir("./Show_me_data_structures_project/testdir"))

contents = os.listdir(".")
# Let us check if this file is indeed a file!
print (os.path.isfile("./ex.py"))

# for item in contents:
#     print("{},{}".format(item,os.path.isdir(item)))

# Does the file end with .py?
print ("./ex.py".endswith(".py"))