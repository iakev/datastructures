def tower_of_Hanoi1(num_disks,rodA,rodB,rodC):
    """
    :param: num_disks - number of disks
    TODO: print the steps required to move all disks from source to destination
    """
    #Termination condition
    if num_disks == 1:
        steps(rodA,rodC) # termination stage 
        return
    
    rodB,rodC = switch(rodB,rodC)
    tower_of_Hanoi(num_disks-1,rodA,rodB,rodC)
    steps(rodA,rodB) 
    rodB,rodC = switch(rodB,rodC)
    # if 
    tower_of_Hanoi(num_disks-1, "A",rodB,rodC)
    
def steps(rodA,rodB):
    print(rodA+" "+rodB)

def switch(rodA,rodB):
     temp = rodA
     rodA = rodB
     rodB = temp 
     return (rodA,rodB)  
    
#########################################Udacity Solution#############################################################
# Recursive Solution
def tower_of_Hanoi_soln(num_disks, source, auxiliary, destination):
    
    # Base condition
    if num_disks == 0:
        return

    # Termination condition
    if num_disks == 1:
        print("{} {}".format(source, destination))
        return
    

    '''Just think of one iteration, rest the Recursion will take care!'''
    
    # Step 1: Move `num_disks - 1` from source to auxiliary
    tower_of_Hanoi_soln(num_disks - 1, source, destination, auxiliary)
    
    # Step 2: Now you are left with the only largest disk at source. 
    # Move the only leftover disk from source to destination
    print("{} {}".format(source, destination))
    
    # Step 3: Move `num_disks - 1` from auxiliary to destination
    tower_of_Hanoi_soln(num_disks - 1, auxiliary, source, destination)
    
def tower_of_Hanoi(num_disks):
    tower_of_Hanoi_soln(num_disks, 'S', 'A', 'D')



tower_of_Hanoi(3)
