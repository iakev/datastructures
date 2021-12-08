def permutations(string):
    """
    :param: input string
    Return - list of all permutations of the input string
    TODO: complete this function to return a list of all permutations of the string
    """
    
    if len(string) == 0:
        ls = []
        return ls
    else:
        first = string[0]
        substr = string[1:]
        ls = permutations(substr)
        if len(ls) == 0:
            ls.append(first)
            return ls
        else:
            ls1 = []
            for i in ls:
                for j in range(len(i)+1):
                    ilist = list(i)
                    ilist.insert(j,first)
                    str1 = ''.join(ilist)
                    ls1.append(str1)
            ls = ls1

        return ls

# Udacity Solution


def permutations2(string):
    return return_permutations(string, 0)
    
def return_permutations(string, index):
    # output to be returned 
    output = list()
    
    # Terminaiton / Base condition
    if index >= len(string):
        return [""]
    
    # Recursive function call
    small_output = return_permutations(string, index + 1)
    
    # Pick a character
    current_char = string[index] 
    
    # Iterate over each sub-string available in the list returned from previous call
    for subString in small_output:
        
        # place the current character at different indices of the sub-string
        for index in range(len(small_output[0]) + 1):
            
            # Make use of the sub-string of previous output, to create a new sub-string. 
            new_subString = subString[0: index] + current_char + subString[index:]
            output.append(new_subString)

    return output



    



print(permutations2("abc"))