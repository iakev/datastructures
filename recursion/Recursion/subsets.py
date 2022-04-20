# import copy
# def subsets(arr):
#     """
#     :param: arr - input integer array
#     Return - list of lists (two dimensional array) where each list represents a subset
#     TODO: complete this method to return subsets of an array
#     """
#     output = list()
#     output = recursive_sub(arr)
#     return output

    

# def recursive_sub(arr):
#     # if arr == []:
#     #     first = None
#     #     return []

#     # first = arr[0]
#     # input_arr = [first]
#     # rest = slice(1,len(arr)+1,1)
#     # remainder = arr[rest]
#     # sub = recursive_sub(remainder)
#     # newarr = copy.deepcopy(sub)
#     # if sub == []:
#     #     newarr = [newarr]
#     # last = copy.deepcopy(newarr[-1])
#     # last.append(first)
#     # newarr.append(last)
#     # if remainder != []:
#     #     newarr.append(remainder)
    
#     # print(newarr)
#     # return newarr
#     output = []
#     if arr == []:
#         return []
#     first = arr.pop()
#     sub = recursive_sub(arr)
#     output.append(sub)
#     if len(output) <= 3:
#         output.append([first])

#     return output

###############UDACITY IMPLEMENTATION##############################
def subsets(arr):
    return return_subsets(arr, 0)

def return_subsets(arr, index):
    if index >= len(arr):
        return [[]]

    small_output = return_subsets(arr, index + 1)

    output = list()
    # append existing subsets
    for element in small_output:
        output.append(element)

    # add current elements to existing subsets and add them to the output
    for element in small_output:
        current = list()
        current.append(arr[index])
        current.extend(element)
        output.append(current)
    return output    

subsets([9,9])