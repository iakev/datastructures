#Using deep copy for the compuond list
import sys
import copy


def permute(inputList):
    """
    Args: myList: list of items to be permuted
    Returns: list of permutation with each permuted item being represented by a list
    """
    complist = []
    ls = []
    #base_case
    if type(inputList[0]) != int and len(inputList[0]) == 0: #still base case
        return
    #initial case
    if type(inputList[0]) == int: # needs to be the final case before base case
        item  = inputList[-1]
        ls.append(item)
        rest = slice(0,len(inputList)-1)
        sublist = inputList[rest]
        complist.append(sublist)
        complist.append(ls)
    # identifyig input to my recursive call
    else:                                          #needs to be the initial cases
        item = inputList[0][-1]
        # item = inputList[0]
        newlist = copy.deepcopy(inputList[1:])
        # newlist = copy.deepcopy(inputList[:])
        # if len(inputList[-1]) == 1:
        if len(inputList) == 1:
            for i in range(2*len(inputList[-1])):
                ls = copy.deepcopy(inputList[-1])
                ls.insert(i,item)
                complist.append(ls)
        else:
            for i in newlist:
                for j in range (len(i)+1):
                    ls = copy.deepcopy(i)
                    ls.insert(j,item)
                    complist.append(ls)

        rest = slice(0,len(inputList[0])-1)
        sublist = inputList[0][rest]
        complist = [sublist] + complist
        
    permute(complist)
    complist = complist[1:]
    return complist 



    
             

    # compList.append(ls)
    # item  = inputList[-1]
    # # ls.append(item)
    # # # compList.append(ls)
    # for i in range (2*len(inputList)):
    #     compList.append([])
    
def permute2(inputList):
    """
    Args: myList: list of items to be permuted
    Returns: list of permutation with each permuted item being represented by a list
    """
    if len(inputList) == 0: #when inputList is empty
        return [[]]

    if len(inputList) == 1: #last recursive call condition
        complist = []
        complist.append(inputList)
        return complist  #base case also
    sublist = inputList[1:]
    complist = copy.deepcopy(permute2(sublist)) #recursive call
    item = inputList[0] #getting next element of the input starting from the last to the first

    if len(complist[0]) == 1: #initial case of building compound list with one element present currently
        for i in range (len(inputList)):
            if len(complist[0]) == 1:
                ls = copy.deepcopy(complist[0])
                ls.insert(i,item)
                complist.append(ls)
    else: #building compund list after initial build incrementally according to previous list results
        items = copy.deepcopy(complist)
        for i in items: 
            for j in range(len(i)+1):
                ls = copy.deepcopy(i)
                ls.insert(j,item)
                complist.append(ls)
    if len(complist[0]) == 1:    
        complist.pop(0)
    else:     
        i = 0
        while i < len(complist): #postprocessing compound list as required
            if len(complist[i]) != len(complist[-1]):
                complist.pop(i)
                i = 0
                continue
            i += 1
    return complist

print(permute2([]))

def permute3(inputList):
    
    # a compound list
    finalCompoundList = []                  # compoundList to be returned 
    
    # Terminaiton / Base condition
    if len(inputList) == 0:
        finalCompoundList.append([])
        
    else:
        first_element = inputList[0]        # Pick one element to be permuted
        after_first = slice(1, None)        # `after_first` is an object of type 'slice' class
        rest_list = inputList[after_first]  # convert the `slice` object into a list
        
        # Recursive function call
        sub_compoundList = permute3(rest_list)
        
        # Iterate through all lists of the compoundList returned from previous call
        for aList in sub_compoundList:
            
            # Permuted the `first_element` at all positions 0, 1, 2 ... len(aList) in each iteration
            for j in range(0, len(aList) + 1): 
                
                # A normal copy/assignment will change aList[j] element
                bList = copy.deepcopy(aList)  
                
                # A new list with size +1 as compared to aList
                # is created by inserting the `first_element` at position j in bList
                bList.insert(j, first_element)
                
                # Append the newly created list to the finalCompoundList
                finalCompoundList.append(bList)
                
    return finalCompoundList

print(permute3([0,1,2]))