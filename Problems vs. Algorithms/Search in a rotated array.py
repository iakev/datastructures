# %%
def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if input_list == []:
        return -1
    
    return binary_search(input_list,number,0,len(input_list)-1)
    
def binary_search(arr,target,start,end):
    mid = start + ((end - start) // 2)

    # base cases
    if arr[mid] == target:
        return mid

    elif start > end:
        return -1

    # Taking care of instances immediately before and after mid index
    elif arr[mid -1] == target:
        return mid - 1

    elif (mid + 1) < len(arr)-1 and arr[mid + 1] == target:
        return mid + 1

    #recursive cases
    else:

        if arr[mid] >= target and arr[start] <= target:
            #we discard the first half and recurse on the other half and vice versa in the else case
            end =  mid

        else:
            #if mid element is just next to a pivot
            start = mid + 1
            

        index = binary_search(arr,target,start,end)

    return index

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


# %%
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    # rotated_array_search(input_list, number)
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")



# %%
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# print pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# print pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# print pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
# print pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# print pass
test_function([[], 10])
# print pass
