
# %%
def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 1:
        return [input_list[0],input_list[0]]

    elif input_list == []:
        return [None,None]

    quicksort(input_list)  #in-place sorting

    first_int = ""
    second_int = ""

    for i in range(len(input_list)-1,-1,-2):
        first_int += str(input_list[i])
        if i-1 != -1: 
            second_int += str(input_list[i-1])
            

    return [int(first_int),int(second_int)]

def quicksort(input_list):
    start_index = 0
    end_index = len(input_list)-1

    sort_all(input_list,start_index,end_index)

def sort_all(input_list,start_index,end_index):

    if end_index <= start_index:
        return

    pivot_index = sort_a_bit(input_list,start_index,end_index)
    sort_all(input_list,start_index,pivot_index-1)
    sort_all(input_list,pivot_index+1,end_index)

def sort_a_bit(input_list,start_index,end_index):

    left_index = start_index
    pivot_index = end_index
    pivot_value = input_list[pivot_index]

    

    while (pivot_index != left_index):
        item = input_list[left_index]

        if input_list[left_index] <= pivot_value:
            left_index += 1
            continue

        input_list[left_index] = input_list[pivot_index-1]

        input_list[pivot_index - 1] = pivot_value

        input_list[pivot_index] = item

        pivot_index -= 1

    return pivot_index

# %%
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if output[0] != None:
        if sum(output) == sum(solution):
            print("Pass")
        else:
            print("Fail")

    if output == [None,None]:
        print("Pass") 

# %%
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
# prints pass
# %%
test_case = [[1, 2, 3, 4, 5], [542, 31]]
test_function(test_case)
# prints pass
# %%
test_case = [[8,3,1,7,9,2],[972,831]]
test_function(test_case)
# prints pass

# %%
test_case = [[0],[0,0]]
test_function(test_case)
# prints pass
# %%
test_case = [[],[None,None]]
test_function(test_case)
# prints pass