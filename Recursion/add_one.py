def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    borrow = 1
    if len(arr) == 0:
        return [1]    
    digit = borrow + arr[-1]
    borrow = digit // 10
    if borrow == 0:
        arr[-1] = digit
        return arr

    else:
        if len(arr) > 0:
            borrow = digit % 10
        subarr = arr[slice(0,len(arr)-1)]
        return  add_one(subarr) + [borrow]

print(add_one([9,9,9,9]))

def add_one2(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    # Base case 
    if arr == [9]:
        return [1, 0]
    
    # A simple case, where we just need to increment the last digit
    if arr[-1] < 9:
        arr[-1] += 1

    # Case when the last digit is 9.
    else:
        '''Recursive call'''
        # We have used arr[:-1], that means all elements of the list except the last one.
        # Example, for original input arr=[1,2,9], we will pass [1,2] in next call.
        arr = add_one(arr[:-1]) + [0]
        
    return arr

