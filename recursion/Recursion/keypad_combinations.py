def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""

def characters_list(num):
    numstr = str(num)
    chars = []
    for i in numstr:
        chars.append(get_characters(int(i)))
    return chars

def keypad(num):
    
    # TODO: Write your keypad solution here!
    chars = characters_list(num)
    output = list()
    output = recursive_keypad(chars)
    return output

def recursive_keypad(lis):

    min_output = []
    str1 = ''
    #base case
    if len(lis) == 0:
        return 

    #recursive call
    first_chars = lis.pop(0)

    min_output = recursive_keypad(lis)

    if min_output is None:
        lis.append(first_chars)
        return lis    
    else:
        if len(lis) == 1:
            min_output = lis.pop()
        ls1 = []
        for c in first_chars:
            for d in min_output:
                str1 = c+d
                ls1.append(str1)
        return ls1

    
#Udacity solution--------------------------------------------------------------------
# Recursive Solution
def keypad2(num):
    
    # Base case
    if num <= 1:
        return [""]

    # If `num` is single digit, get the LIST having one element - the associated string
    elif 1 < num <= 9:
        return list(get_characters(num))

    # Otherwise `num` >= 10. Find the unit's (last) digits of `num` 
    last_digit = num % 10
    
    '''Step 1'''
    # Recursive call to the same function with “floor” of the `num//10`
    small_output = keypad2(num//10)               # returns a LIST of strings
    
    '''Step 2'''
    # Get the associated string for the `last_digit`
    keypad_string = get_characters(last_digit)   # returns a string
    
    '''Permute the characters of result obtained from Step 1 and Step 2'''
    output = list()

    '''
    The Idea:
    Each character of keypad_string must be appended to the 
    end of each string available in the small_output
    '''
    for character in keypad_string:
        for item in small_output:
            new_item = item + character
            output.append(new_item)
    
    return output    


print(keypad(23))
print(keypad(32))
print(keypad(8))
print(keypad2(353))