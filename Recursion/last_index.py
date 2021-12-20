# def recursive_last_index(arr,index,target):
#     if arr == target:
#         return index


def last_index(arr, target):
    """
    :param: arr - input array
    :param: target - integer element
    return: int - last index of target in arr
    TODO: complete this method to find the last index of target in arr
    """
    index=recursive_index(arr,0,target)
    
    return index

def recursive_index(arr,i,target):
    # implementing base case when target not present in the whole array
    if len(arr) == 0:
        return -1
    first = arr[0]
    current_index = -2
    #case when the last element is equal to the target
    # if len(arr) == 1 and first == target:
    #     return i

    sub = slice(1,len(arr)+1,1)
    rest = arr[sub]
    if first == target:
        current_index = i
    # indice = i
    index =recursive_index(rest,i=i+1,target=target)
    # if index == -1:    
    #     return index

    if current_index > index:
        index = current_index
    else:
        index = index
    
    return index

print(last_index([1, 2, 5, 5, 1, 2, 5, 4],7))

##################################Udacity Solution###############################################
def last_index(arr, target):
    # we start looking from the last index
    return last_index_arr(arr, target, len(arr) - 1)


def last_index_arr(arr, target, index):
    if index < 0:
        return -1
    
    # check if target is found
    if arr[index] == target:
        return index

    # else make a recursive call to the rest of the array
    return last_index_arr(arr, target, index - 1)