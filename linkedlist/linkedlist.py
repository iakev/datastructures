# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None
        
#     def append(self, value):
#         if self.head is None:
#             self.head = Node(value)
#             return
        
#         # Move to the tail (the last node)
#         node = self.head
#         while node.next:
#             node = node.next
        
#         node.next = Node(value)
#         return
    
#     def to_list(self):
        
#         # TODO: Write function to turn Linked List into Python List
#         lis = []

#         current_node = self.head
        
#         while current_node.next is not None:
#             lis.append(current_node.value)
#             current_node = current_node.next
        
#         lis.append(current_node.value)
#         return lis

# linked_list = LinkedList()
# linked_list.append(3)
# linked_list.append(2)
# linked_list.append(-1)
# linked_list.append(0.2)
# linked_list.to_list()


# class DoubleNode:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#         self.previous = None

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
    
#     def append(self, value):
        
#         # TODO: Implement this method to append to the tail of the list
#         if self.head is None:
#             self.head = DoubleNode(value)
#             self.tail = self.head
#             return
        
#         self.tail.next = DoubleNode(value)
#         self.tail.previous = self.tail
#         self.tail = self.tail.next
#         return
        

# linkedlist = DoublyLinkedList()
# linkedlist.append(1)
# linkedlist.append(-2)
# linkedlist.append(4)


####################################################################
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def to_list(self):
#         out = []
#         node = self.head
#         while node:
#             out.append(node.value)
#             node = node.next
#         return out


# # Define a function outside of the class
# def prepend(self, value):
#     """ Prepend a value to the beginning of the list. """
#     # TODO: Write function to prepend here
#     if self.head is not None:
#         node_next = self.head
#         self.head = Node(value)
#         self.head.next = node_next
#     else:
#         self.head = Node(value)


# # This is the way to add a function to a class after it has been defined
# LinkedList.prepend = prepend

# def append(self, value):
#     """ Append a value to the end of the list. """    
#     # TODO: Write function to append here    
#     if self.head is None:
#         self.head = Node(value)
#         return
    

#     node = self.head

#     while node.next:
#         node = node.next

#     node.next = Node(value)

# LinkedList.append = append

# # Test prepend
# linked_list = LinkedList()
# linked_list.prepend(1)
# assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"


# # Test append - 1
# linked_list.append(3)
# linked_list.prepend(2)
# assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

# def search(self, value):
#     """ Search the linked list for a node with the requested value and return the node. """
#     # TODO: Write function to search here
#     if self.head is None:
#         return None

#     node = self.head

#     while node:
#         if node.value == value:
#             return node
#         node = node.next
    

#     raise ValueError("Value not found in list")


# LinkedList.search = search

# # Test search
# linked_list.prepend(2)
# linked_list.prepend(1)
# linked_list.append(4)
# linked_list.append(3)
# assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
# assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"


# def remove(self, value):
#     """ Remove first occurrence of value. """
#     # TODO: Write function to remove here
#     if self.head is None:
#         return("No value in linked list yet")
    
#     elif self.head.value == value:
#         node = self.head
#         node.next = self.head.next
#         self.head = node.next
#         return
    
#     else:
#         node =self.head
#         curr_node = node
#         while node:
#             if node.value == value:
#                 curr_node.next = node.next
#                 return
#             curr_node = node
#             node = node.next    
#     raise ValueError("Value not found in the list")

# LinkedList.remove = remove
# linked_list.remove(1)

# def pop(self):
#     """ Return the first node's value and remove it from the list. """
#     # TODO: Write function to pop here
#     if self.head is None:
#         return ("No value in linked list yet")

#     else:
#         node = self.head
#         node.next = self.head.next
#         self.head = node.next
#         return node.value

# LinkedList.pop = pop

# linked_list.pop()

# def insert(self, value, pos):
#     """ Insert value at pos position in the list. If pos is larger than the
#     length of the list, append to the end of the list. """
        
#     # TODO: Write function to insert here
#     lis = self.to_list()
#     node = self.head
#     curr_nd = node
#     count = 0
#     if pos == 0:
#         node = Node(value)
#         self.head = node
#         self.head.next = curr_nd
#         count += 1
#         return

#     if pos > len(lis):
#         while node:
#             if node.next is None:
#                 node.next=Node(value)
#                 return
#             node = node.next
    
#     while node:
#         if count == pos:
#             node = Node(value)
#             node.next = curr_nd.next
#             curr_nd.next = node
#             return
#         curr_nd = node
#         node = node.next    
#         count += 1

# LinkedList.insert = insert

# linked_list.insert(5, 0)
# linked_list.insert(2, 1)
# linked_list.insert(3, 6)

# def size(self):
#     """ Return the size or length of the linked list. """
#     # TODO: Write function to get size here
#     lis = self.to_list()
#     return len(lis)

# LinkedList.size = size

###################################################################################

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# #init_list is for instatiating a linked list with a list
# class LinkedList:
#     def __init__(self,init_list=None):
#         self.head = None
#         if init_list:
#             for value in init_list:
#                 self.append(value)


#     def append(self, value):
#         if self.head is None:
#             self.head = Node(value)
#             return
        
#         #Move to tail (last node)
#         node = self.head
#         while node.next:
#             node = node.next

#         node.next = Node(value)
        
#     def __iter__(self):
#         node = self.head
#         while node:
#             yield node.value
#             node = node.next
            
#     def __repr__(self):
#         return str([v for v in self])


# def reverse(linked_list):
#     """
#     Reverse the inputted linked list

#     Args:
#        linked_list(obj): Linked List to be reversed
#     Returns:
#        obj: Reveresed Linked List
#     """
#     new_list = LinkedList()
    
#     prev_node = None

#     """
#     A simple idea - Pick a node from the original linked list traversing form the beginning, and 
#     prepend it to the new linked list. 
#     We have to use a loop to iterate over the nodes of original linked list
#     """
#     # In this "for" loop, the "value" is just a variable whose value will be updated in each iteration
#     for value in linked_list:
#         # create a new node
#         new_node = Node(value)
        
#         # Make the new_node.next point to the 
#         # node created in previous iteration
#         new_node.next = prev_node 
        
#         # This is the last statement of the loop
#         # Mark the current new node as the "prev_node" for next iteration
#         prev_node = new_node
    
#     # Update the new_list.head to point to the final node that came out of the loop
#     new_list.head = prev_node
    
#     return new_list


# def iscircular(linked_list):
#     """
#     Determine wether the Linked List is circular or not

#     Args:
#        linked_list(obj): Linked List to be checked
#     Returns:
#        bool: Return True if the linked list is circular, return False otherwise
#     """

#     if linked_list.head is None:
#         return False
    
#     slow = linked_list.head
#     fast = linked_list.head
    
#     while fast and fast.next:
#         # slow pointer moves one node
#         slow = slow.next
#         # fast pointer moves two nodes
#         fast = fast.next.next
        
#         if slow == fast:
#             return True
    
#     # If we get to a node where fast doesn't have a next node or doesn't exist itself, 
#     # the list has an end and isn't circular
#     return False

# list_with_loop = LinkedList([2, -1, 3, 0, 5])

# # Creating a loop where the last node points back to the second node
# loop_start = list_with_loop.head.next

# node = list_with_loop.head
# while node.next: 
#     node = node.next   
# node.next = loop_start

###############################################################################################################

# A class behaves like a data-type, just like an int, float or any other built-in ones. 
# # User defined class
# class Node:
#     def __init__(self, value): # <-- For simple LinkedList, "value" argument will be an int, whereas, for NestedLinkedList, "value" will be a LinkedList
#         self.value = value
#         self.next = None
    
#     def __repr__(self):
#         return str(self.value)
    
# # User defined class
# class LinkedList: 
#     def __init__(self, head): # <-- Expects "head" to be a Node made up of an int or LinkedList
#         self.head = head
    
#     '''
#     For creating a simple LinkedList, we will pass an integer as the "value" argument
#     For creating a nested LinkedList, we will pass a LinkedList as the "value" argument
#     '''
#     def append(self, value):
        
#         # If LinkedList is empty
#         if self.head is None:
#             self.head = Node(value)
#             return
        
#         # Create a temporary Node object
#         node = self.head
        
#         # Iterate till the end of the currrent LinkedList
#         while node.next is not None:
#             node = node.next
        
#         # Append the newly creataed Node at the end of the currrent LinkedList
#         node.next = Node(value)

        
#     '''We will need this function/method to convert a LinkedList object into a Python list of integers'''
#     def to_list(self):
#         out = []          # <-- Declare a Python list
#         node = self.head  # <-- Create a temporary Node object
        
#         while node:       # <-- Iterate untill we have nodes available
#             out.append(int(str(node.value))) # <-- node.value is actually of type Node, therefore convert it into int before appending to the Python list
#             node = node.next
        
#         return out

# def merge(list1, list2):
#     # TODO: Implement this function so that it merges the two linked lists in a single, sorted linked list.
#     '''
#     The arguments list1, list2 must be of type LinkedList.
#     The merge() function must return an instance of LinkedList.
#     '''
#     merged = LinkedList(None)
#     if list1 is None:
#         return list2
#     if list2 is None:
#         return list1
#     list1_elt = list1.head
#     list2_elt = list2.head
#     while list1_elt is not None or list2_elt is not None:
#         if list1_elt is None:
#             merged.append(list2_elt)
#             list2_elt = list2_elt.next
#         elif list2_elt is None:
#             merged.append(list1_elt)
#             list1_elt = list1_elt.next
#         elif list1_elt.value <= list2_elt.value:
#             merged.append(list1_elt)
#             list1_elt = list1_elt.next
#         else:
#             merged.append(list2_elt)
#             list2_elt = list2_elt.next
#     return merged

# ''' In a NESTED LinkedList object, each node will be a simple LinkedList in itself'''
# class NestedLinkedList(LinkedList):
#     def flatten(self):
#         return self._flatten(self.head) # <-- self.head is a node for NestedLinkedList

#     '''  A recursive function ''' 
#     def _flatten(self, node):
        
#         # A termination condition
#         if node.next is None:
#             return merge(node.value, None) # <-- First argument is a simple LinkedList
        
#         # _flatten() is calling itself untill a termination condition is achieved
#         return merge(node.value, self._flatten(node.next)) # <-- Both arguments are a simple LinkedList each    

# def even_after_odd(head):
    
#     if head is None:
#         return head
    
#     # Helper references
#     ''' `even_head` and `even_tail` represents the starting and current ending of the "EVEN" sub-list '''
#     even_head = None                    
#     even_tail = None
    
#     ''' `odd_head` and `odd_tail` represents the starting and current ending of the "ODD" sub-list '''
#     odd_head = None
#     odd_tail = None
    
#     current = head                  # <-- "current" represents the current Node. 
    
#     # Loop untill there are Nodes available in the LinkedList
#     while current:                  # <-- "current" will be updated at the end of each iteration
        
#         next_node = current.next    # <-- "next_node" represents the next Node w.r.t. the current Node
        
#         if current.data % 2 == 0:   # <-- current Node is even
            
#             # Below 
#             if even_head is None:   # <-- Make the current Node as the starting Node of EVEN sub-list
#                 even_head = current     # `even_head` will now point where `current` is already pointing
#                 even_tail = even_head     
#             else:                   # <-- Append the current even node to the tail of EVEN sub-list 
#                 even_tail.next = current
#                 even_tail = even_tail.next
#         else:
#             if odd_head is None:    # <-- Make the current Node as the starting Node of ODD sub-list
#                 odd_head = current
#                 odd_tail = odd_head
#             else:                   # <-- Append the current odd node to the tail of ODD sub-list 
#                 odd_tail.next = current
#                 odd_tail = odd_tail.next
#         current.next = None
#         current = next_node         # <-- Update "head" Node, for next iteration
    
#     if odd_head is None:            # <-- Special case, when there are no odd Nodes 
#         return even_head

#     odd_tail.next = even_head       # <-- Append the EVEN sub-list to the tail of ODD sub-list
    
#     return odd_head



# def add_one(arr):
#     borrow = 1; # initial value
#     """
#     :param: arr - list of digits representing some number x
#     return a list with digits represengint (x + 1)
 
#     The three arguments of range() function are: 
#     starting index, ending index(non-inclusive), and the increment/decrement value
#     """ 
#     # Traverse in reverse direction starting from the end of the list
#     # The argument of range() functions are:
#     # starting index, ending index (non exclusive), and the increment/decrement size
#     for i in range(len(arr), 0, -1):     
        
#         # The "digit" denotes the updated Unit, Tens, and then Hunderd  position iteratively
#         digit = borrow + arr[i - 1]       
       
#         '''
#         The "borrow" will be carried to the next left digit 
#         If the digit is between 0-9, borrrow will be 0. 
#         If digit is 10, then the borrow will be 1.
#         '''
#         # The "//" is a floor division operator
#         borrow = digit//10               

#         if borrow == 0:
#             # Update the arr[i - 1] with the updated digit, and quit the FOR loop.
#             arr[i - 1] = digit
#             break
#         else:
#             # Update the arr[i - 1] with the remainder of (digit % 10)
#             arr[i - 1] = digit % 10
    
#     # Prepend the final "borrow" to the original array.  
#     arr = [borrow] + arr
    
#     # In this final updated arr, find a position (starting index) from where to return the list.
#     # For [0, 1, 2, 4] , the position (starting index) will be 1
#     # For [1, 0, 0, 0] , the position (starting index) will be 0

#     position = 0
#     while arr[position]==0:
#         position += 1

#     return arr[position:]


# def duplicate_number(arr):
#     current_sum = 0
#     expected_sum = 0
    
#     # Traverse the original array in the forward direction 
#     for num in arr:
#         current_sum += num
    
    
#     # Traverse from 0 to (length of array-1) to get the expected_sum
#     # Alternatively, you can use the formula for sum of an Arithmetic Progression to get the expected_sum
    
#     # The argument of range() functions are:
#     # starting index [OPTIONAL], ending index (non exclusive), and the increment/decrement size [OPTIONAL]
#     # It means that if the array length = n, loop will run form 0 to (n-2)
#     for i in range(len(arr) - 1):
#         expected_sum += i
    
    
#     # The difference between the 
#     return current_sum - expected_sum


# def max_sum_subarray(arr):
    
#     current_sum = arr[0] # `current_sum` denotes the sum of a subarray
#     max_sum = arr[0]     # `max_sum` denotes the maximum value of `current_sum` ever
    
#     # Loop from VALUE at index position 1 till the end of the array
#     for element in arr[1:]:
        
#         '''
#         # Compare (current_sum + element) vs (element)
#         # If (current_sum + element) is higher, it denotes the addition of the element to the current subarray
#         # If (element) alone is higher, it denotes the starting of a new subarray
#         '''
#         current_sum = max(current_sum + element, element)
        
#         # Update (overwrite) `max_sum`, if it is lower than the updated `current_sum`
#         max_sum = max(current_sum, max_sum)   
    
#     return max_sum

# def nth_row_pascal(n):
#     """
#     :param: - n - index (0 based)
#     return - list() representing nth row of Pascal's triangle
#     """
#     lis = [None] * n
#     if n == 0:
#         return [1]
    
#     current_row = [1]

#     for i in range(1,n+1):
#         previous_row = current_row

#         current_row = [1]

#         for j in  range(j,i):
#             next_nummber = previous_row[j] + previous_row[j - 1]
            
#             current_row.append(next_nummber)

#         current_row.append(1)
#     return current_row
        
# def skip_i_delete_j(head, i, j):
#     # Edge case - Skip 0 nodes (means Delete all nodes)
#     if i == 0:
#         return None
    
#     # Edge case - Delete 0 nodes
#     if j == 0:
#         return head
    
#     # Invalid input
#     if head is None or j < 0 or i < 0:
#         return head

#     # Helper references
#     current = head
#     previous = None
    
#     # Traverse - Loop untill there are Nodes available in the LinkedList
#     while current:
        
#         '''skip (i - 1) nodes'''
#         for _ in range(i - 1):
#             if current is None:
#                 return head
#             current = current.next
#         previous = current
#         current = current.next
        
#         '''delete next j nodes'''
#         for _ in range(j):
#             if current is None:
#                 break
#             next_node = current.next
#             current = next_node
        
#         '''Connect the `previous.next` to the `current`''' 
#         previous.next = current
    
#     # Loop ends
    
#     return head        
            

def swap_nodes(head, position_one, position_two):

    # If both the indices are same
    if position_one == position_two:
        return head
    
    # Helper references
    one_previous = None
    one_current = None

    two_previous = None
    two_current = None

    current_index = 0
    current_node = head 
    new_head = None

    # LOOP - find out previous and current node at both the positions (indices)
    while current_node is not None:
        
        # Position_one cannot be equal to position_two, 
        # so either one of them might be equal to the current_index
        if current_index == position_one:
            one_current = current_node
        
        elif current_index == position_two:
            two_current = current_node
            break

        # If neither of the position_one or position_two are equal to the current_index
        if one_current is None:
            one_previous = current_node
        
        two_previous = current_node
        
        # increment both the current_index and current_node
        current_node = current_node.next         
        current_index += 1
        

    # Loop ends
    
    
    '''SWAPPING LOGIC'''
    # We have identified the two nodes: one_current & two_current to be swapped, 
    # Make use of a temporary reference to swap the references
    two_previous.next = one_current
    temp = one_current.next
    one_current.next = two_current.next
    two_current.next = temp
    
    # if the node at first index is head of the original linked list
    if one_previous is None:
        new_head = two_current
    else:
        one_previous.next = two_current
        new_head = head
    # Swapping logic ends
    
    return new_head