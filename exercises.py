# courses = {
#     'spring2020': { 'cs101': {'name': 'Building a Search Engine',
#                            'teacher': 'Dave',
#                            'assistant': 'Peter C.'},
#                  'cs373': {'name': 'Programming a Robotic Car',
#                            'teacher': 'Sebastian',
#                            'assistant': 'Andy'}},
#     'fall2020': { 'cs101': {'name': 'Building a Search Engine',
#                            'teacher': 'Dave',
#                            'assistant': 'Sarah'},
#                  'cs212': {'name': 'The Design of Computer Programs',
#                            'teacher': 'Peter N.',
#                            'assistant': 'Andy',
#                            'prereq': 'cs101'},
#                  'cs253': {'name': 'Web Application Engineering - Building a Blog',
#                            'teacher': 'Steve',
#                            'prereq': 'cs101'},
#                  'cs262': {'name': 'Programming Languages - Building a Web Browser',
#                            'teacher': 'Wes',
#                            'assistant': 'Peter C.',
#                            'prereq': 'cs101'},
#                  'cs373': {'name': 'Programming a Robotic Car',
#                            'teacher': 'Sebastian'},
#                  'cs387': {'name': 'Applied Cryptography',
#                            'teacher': 'Dave'}},
#     'spring2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
#                            'teacher': 'Dorina'},
#                         'cs003': {'name': 'Programming a Robotic Robotics Teacher',
#                            'teacher': 'Jasper'},
#                      }
#     }


# def when_offered(courses, course):
#     # TODO: Fill out the function here.
#     # for key in courses:
#         # if course == courses[key]
        
#     # TODO: Return list of semesters here.
    
#     return None



# print(when_offered(courses, 'cs101'))
# # Correct result: 
# # ['fall2020', 'spring2020']

# print(when_offered(courses, 'bio893'))
# # Correct result: 
# # # []
# correct = [[1,2,3],
#            [2,3,1],
#            [3,1,2]]

# incorrect = [[1,2,3,4],
#              [2,3,1,3],
#              [3,1,2,3],
#              [4,4,4,4]]

# incorrect2 = [[1,2,3,4],
#              [2,3,1,4],
#              [4,1,2,3],
#              [3,4,1,2]]

# incorrect3 = [[1,2,3,4,5],
#               [2,3,1,5,6],
#               [4,5,2,1,3],
#               [3,4,5,2,1],
#               [5,6,4,3,2]]

# incorrect4 = [['a','b','c'],
#               ['b','c','a'],
#               ['c','a','b']]

# incorrect5 = [ [1, 1.5],
#                [1.5, 1]]

# def check_sudoko(square):

    # column = []
    # size = len(square)
    # for i in range(size):
    #     for j in range(size):
    #         if type(square[i][j]) == str or (not square[i][j].is_integer()): 
    #             return False
    #         elif square[i][j] > size or square[i][j] <= 0:
    #             return False
    #         elif square[i].count(j) > 1: #assuring uniqueness in rows
    #             return False
    #         elif square[j][i] > 0 and square[j][i] <=size:
    #             column.append(square[j][i])
    #         elif column.count(j) > 1:
    #             return False
    #         else:
    #             return True

# class Person:
#     def __init__(self, name, age, month):
#         self.name = name
#         self.age = age
#         self.birthday_month = month
        
#     def birthday(self):
#         self.age += 1

# def create_person_objects(names, ages, months):
#     my_data = zip(names, ages, months)
#     person_objects = []
#     for item in my_data:
#         person_objects.append(Person(*item))
#     return person_objects

# def get_april_birthdays(people):
#     # TODO:
#     # Increment "age" for all people with birthdays in April.
#     # Return a dictionary "april_birthdays" with the names of
#     # all people with April birthdays as keys, and their updated ages 
#     # as values. See the test below for an example expected output.
#     april_birthdays = {}

    
#     # TODO: Modify the return statement 
#     return

# def get_most_common_month(people):
#     # TODO:
#     # Use the "months" dictionary to record counts of birthday months
#     # for persons in the "people" data.
#     # Return the month with the largest number of birthdays.
#     months = {'January':0, 'February':0, 'March':0, 'April':0, 'May':0, 
#               'June':0, 'July':0, 'August':0, 'September':0, 'October':0,
#               'November':0, 'December':0}
    
#     # TODO: Modify the return statement.
#     return


# def test():
#     # Here is the data for the test. Assume there is a single most common month.
#     names = ['Howard', 'Richard', 'Jules', 'Trula', 'Michael', 'Elizabeth', 'Richard', 'Shirley', 'Mark', 'Brianna', 'Kenneth', 'Gwen', 'William', 'Rosa', 'Denver', 'Shelly', 'Sammy', 'Maryann', 'Kathleen', 'Andrew', 'Joseph', 'Kathleen', 'Lisa', 'Viola', 'George', 'Bonnie', 'Robert', 'William', 'Sabrina', 'John', 'Robert', 'Gil', 'Calvin', 'Robert', 'Dusty', 'Dario', 'Joeann', 'Terry', 'Alan', 'Rosa', 'Jeane', 'James', 'Rachel', 'Tu', 'Chelsea', 'Andrea', 'Ernest', 'Erica', 'Priscilla', 'Carol', 'Michael', 'Dale', 'Arthur', 'Helen', 'James', 'Donna', 'Patricia', 'Betty', 'Patricia', 'Mollie', 'Nicole', 'Ernest', 'Wendy', 'Graciela', 'Teresa', 'Nicole', 'Trang', 'Caleb', 'Robert', 'Paul', 'Nieves', 'Arleen', 'Milton', 'James', 'Lawrence', 'Edward', 'Susan', 'Patricia', 'Tana', 'Jessica', 'Suzanne', 'Darren', 'Arthur', 'Holly', 'Mary', 'Randal', 'John', 'Laura', 'Betty', 'Chelsea', 'Margaret', 'Angel', 'Jeffrey', 'Mary', 'Donald', 'David', 'Roger', 'Evan', 'Danny', 'William']
#     ages  = [17, 58, 79, 8, 10, 57, 4, 98, 19, 47, 81, 68, 48, 13, 39, 21, 98, 51, 49, 12, 24, 78, 36, 59, 3, 87, 94, 85, 43, 69, 15, 52, 57, 36, 52, 5, 52, 5, 33, 10, 71, 28, 70, 9, 25, 28, 76, 71, 22, 35, 35, 100, 9, 95, 69, 52, 66, 91, 39, 84, 65, 29, 20, 98, 30, 83, 30, 15, 88, 89, 24, 98, 62, 94, 86, 63, 34, 23, 23, 19, 10, 80, 88, 67, 17, 91, 85, 97, 29, 7, 34, 38, 92, 29, 14, 52, 94, 62, 70, 22]
#     months = ['January', 'March', 'January', 'October', 'April', 'February', 'August', 'January', 'June', 'August', 'February', 'May', 'March', 'June', 'February', 'August', 'June', 'March', 'August', 'April', 'April', 'June', 'April', 'June', 'February', 'September', 'March', 'July', 'September', 'December', 'June', 'June', 'August', 'November', 'April', 'November', 'August', 'June', 'January', 'August', 'May', 'March', 'March', 'March', 'May', 'September', 'August', 'April', 'February', 'April', 'May', 'March', 'March', 'January', 'August', 'October', 'February', 'November', 'August', 'June', 'September', 'September', 'January', 'September', 'July', 'July', 'December', 'June', 'April', 'February', 'August', 'September', 'August', 'February', 'April', 'July', 'May', 'November', 'December', 'February', 'August', 'August', 'September', 'December', 'February', 'March', 'June', 'December', 'February', 'May', 'April', 'July', 'March', 'June', 'December', 'March', 'July', 'May', 'September', 'November']
#     people = create_person_objects(names, ages, months)

#     # Calls to the two functions you have completed.
#     print(get_april_birthdays(people))
#     print(get_most_common_month(people))



# test()
# Expected result:
# {'Michael': 11, 'Erica': 72, 'Carol': 36, 'Lisa': 37, 'Lawrence': 87, 'Joseph': 25, 'Margaret': 35, 'Andrew': 13, 'Dusty': 53, 'Robert': 89}
# August


# def nextDay(year, month, day):
#     """Complete version:  every month has correct days"""
#     if day < daysInMonth(year,month):
#         return year, month, day + 1
#     else:
#         if month == 12:
#             return year + 1, 1, 1
#         else:
#             return year, month + 1, 1

# def dateIsBefore(year1,month1,day1,year2,month2,day2):

#     if year1 < year2:
#         return True
#     if year1 == year2:
#         if month1 < month2:
#             return True
#         if month1 == month2:
#             return day1 < day2
#     return False        

# def daysBetweenDates(year1, month1, day1, year2, month2, day2):
#     """Returns the number of days between year1/month1/day1
#        and year2/month2/day2. Assumes inputs are valid dates
#        in Gregorian calendar, and the first date is not after
#        the second."""
#     # YOUR CODE HERE!
#     assert not (dateIsBefore(year2,month2,day2,year1,month1,day1)),"Input invalid date1 > date2"
#     days = 0
#     while dateIsBefore(year1,month1,day1,year2,month2,day2):
#         year1,month1,day1 = nextDay(year1,month1,day1)
#         days +=1
#     return days
    
# def daysInMonth(year,month):
#     """Returns correct days in a month for all years"""
#     if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month  == 10 or month == 12:
#         return 31
#     elif month == 2:
#         if isLeapYear(year):
#             return 29
#         else:
#             return 28
#     else:
#         return 30

# def isLeapYear(year):
#     """function to check whether year is leap or not"""
#     if year % 4 == 0:
#         leap = True
#         if year % 100 != 0 or year % 400 ==0:
#             leap =  True
#         else:
#             leap = False
#     else:
#         leap = False
#     return leap


# """"Working on reverse string"""
# str = "water"
# str1 = ""
# last = -1
# for i in range(len(str)):
#     str1 += str[last]
#     last -= 1


# def anagram(str1,str2):
#     if len(str1) != len(str2):
#         cleanStr1 = str1.replace(" ","").lower()
#         cleanStr2 = str2.replace(" ","").lower()

#     if sorted(cleanStr1) == sorted(cleanStr2):
#         return True

#     return False

# def word_flipper(our_string):

    # """
    # Flip the individual words in a sentence

    # Args:
    #    our_string(string): String with words to flip
    # Returns:
    #    string: String with words flipped
    # """
    
    # # TODO: Write your solution here
    # #Consider using join method on string and use one for loop
    # strlist = our_string.split(" ")
    # newwords = []
    # flipstr = ""
    
    # for word in strlist:
    #     new_word = ""
    #     for i in range(len(word)):
    #         # Grab the charecter from the back of the string and add them to the new string
    #         new_word += word[(len(word)-1)-i]
    #     newwords.append(new_word)

    # for i in range(len(newwords)):
    #     if i == len(newwords) - 1:
    #         flipstr += newwords[i]
    #     else:
    #         flipstr += newwords[i] + " " 

    # return flipstr

def hamming_distance(str1, str2):

    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """
    
    # TODO: Write your solution here
    
    if len(str1) == len(str2):
        count = 0
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                pass
            else:
                count += 1
    else:
        count =  None


    return count

hamming_distance('Slot machines', 'Cash lost in me')

def add_one(arr):
    borrow = 1; # initial value
    
    """ 
    The three arguments of range() function are: 
    starting index, ending index(non-inclusive), and the increment/decrement value
    """ 
    # Traverse in reverse direction starting from the end of the list
    # The argument of range() functions are:
    # starting index, ending index (non exclusive), and the increment/decrement size
    for i in range(len(arr), 0, -1):     
        
        # The "digit" denotes the updated Unit, Tens, and then Hunderd  position iteratively
        digit = borrow + arr[i - 1]       
       
        '''
        The "borrow" will be carried to the next left digit 
        If the digit is between 0-9, borrrow will be 0. 
        If digit is 10, then the borrow will be 1.
        '''
        # The "//" is a floor division operator
        borrow = digit//10               

        if borrow == 0:
            # Update the arr[i - 1] with the updated digit, and quit the FOR loop.
            arr[i - 1] = digit
            break
        else:
            # Update the arr[i - 1] with the remainder of (digit % 10)
            arr[i - 1] = digit % 10
    
    # Prepend the final "borrow" to the original array.  
    arr = [borrow] + arr
    
    # In this final updated arr, find a position (starting index) from where to return the list.
    # For [0, 1, 2, 4] , the position (starting index) will be 1
    # For [1, 0, 0, 0] , the position (starting index) will be 0
    position = 0
    while arr[position]==0:
        position += 1

    return arr[position:]