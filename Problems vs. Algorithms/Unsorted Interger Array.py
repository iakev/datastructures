# %%
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 1:
        return (ints[0],ints[0])

    if ints == []:
        return (None,None)
        
    min = fastSelect(ints,1)
    max = fastSelect(ints,len(ints))

    return (min,max)

import math #for using math.ceil

def fastSelect(Arr, k):
    #Breaking Arr into [n/5] groups
    groups = {} #dictionary to store the broken up groups
    group_name = "group_"
    no_of_grps = math.ceil(len(Arr)/5)
    elemnts_in_group = int(len(Arr)/no_of_grps)
    count = 1
    for i in range(0,len(Arr),elemnts_in_group):
        if len(groups.values()) == no_of_grps:
            groups[group_name+str(count-1)].append(Arr[i])
            continue
        groups[group_name + str(count)] = [Arr[j] for j in range(i,i+elemnts_in_group)] 
        count += 1

    #For each of the groups above we sort them,find their medians,and add the median to a new list
    
    medians = []
    for group in groups:
        groups[group].sort()
        median = groups[group][len(groups[group])//2]
        medians.append(median)

    # Finding a good pivot for our algorithm recursively
    if len(medians) == 1:
        pivot = medians[0]

    elif (len(medians) > 1):
        pivot = fastSelect(medians,len(medians)//2)


    #Partitioning originl array into three sub-arrays as informed by the good pivot
    Arr_less_p = []
    Arr_equal_p = []
    Arr_greater_p = []
    
    for i in Arr:
        if i < pivot:
            Arr_less_p.append(i)

        elif i == pivot:
            Arr_equal_p.append(i)

        else:
            Arr_greater_p.append(i)

    #perform recursion based on sizes of our three sub-arrays

    if k <= len(Arr_less_p):
       return fastSelect(Arr_less_p,k)

    elif k > (len(Arr_equal_p)+len(Arr_less_p)):
       return fastSelect(Arr_greater_p, (k-(len(Arr_equal_p)+len(Arr_less_p))))

    else:
        return pivot



## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
# prints pass


# %%
import random

l = [i for i in range(0, 100,10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 90) == get_min_max(l)) else "Fail")
# prints pass
# %%
import random

l = [1]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((1,1) == get_min_max(l)) else "Fail")
# prints pass
# %%
l = []

print ("Pass" if ((None,None) == get_min_max(l)) else "Fail")
# prints pass