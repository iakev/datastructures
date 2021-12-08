def tower_of_Hanoi(num_disks):
    """
    :param: num_disks - number of disks
    TODO: print the steps required to move all disks from source to destination
    """
    if num_disks == 1:
        print("S D")
        num_disks -= 1
        return num_disks
    else:
        rest = num_disks - 1
        print("S A")
        num_disks = num_disks -  rest
        num_disks = tower_of_Hanoi(num_disks)
        print("A D")


tower_of_Hanoi(3)