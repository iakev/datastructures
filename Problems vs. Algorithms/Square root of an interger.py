# %%
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        return None

    l = [i for i in range(1,number+1)]

    return binary_search(l,number,0,number)

    
def binary_search(arr,target,start,end):
    
    mid = start + ((end - start) // 2)

    # base cases

    if target == 0:
        return 0

    if (target // arr[mid]) == arr[mid]:
        return arr[mid]

    #recursive cases
    else:

        if arr[mid] * arr[mid] > target:
            #we discard the last half and recurse on the first half and vice versa in the else case
            end =  mid

        else:
            start = mid + 1
            

        root = binary_search(arr,target,start,end)

    return root


#test cases

print ("Pass" if  (3 == sqrt(9)) else "Fail")
# print pass
print ("Pass" if  (0 == sqrt(0)) else "Fail")
# print pass
print ("Pass" if  (4 == sqrt(16)) else "Fail")
# print pass
print ("Pass" if  (1 == sqrt(1)) else "Fail")
# print pass
print ("Pass" if  (5 == sqrt(27)) else "Fail")
# print pass
print ("Pass" if  (8 == sqrt(64)) else "Fail")
# print pass
print ("Pass" if  (None == sqrt(-64)) else "Fail")
# print pass
