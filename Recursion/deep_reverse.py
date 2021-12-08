def deep_reverse(arr):
    
    if len(arr) < 1:
        return arr


    reversed_arr = []

    for i in range(len(arr)-1,-1,-1):
        if type(arr[i]) == list:
            rev_arr = deep_reverse(arr[i])
            reversed_arr.append(rev_arr)
        else:
            reversed_arr.append(arr[i])
        

    return reversed_arr

# Udacity solution---------------------------------------------

def deep_reverse2(arr):
    
    # Terminaiton / Base condition
    if len(arr) < 1:
        return arr

    reversed_items = []  # final list to be returned
    
    '''Traverse the given list (array) in the reverse direction using extended slice.'''
    # For a given list, sample syntax are - myList[1:10:2], myList[:-1:1], myList[::-1]
    # The first argument is the starting index of the slice (inclusive),
    # second argument is the ending index of the slice (exclusive),
    # third argument is the increment/decrement step size.
    # If we do not specify an argument, it means to consider all elements from that end of the list. 
    for item in arr[::-1]:
        
        # If this item is a list itself, invoke deep_reverse to reverse the items recursively.
        if type(item) is list:
            item = deep_reverse2(item)
        
        # append the item to the final list
        reversed_items.append(item)

    return reversed_items


print(deep_reverse([1,2,[3,4,5],4,5]))