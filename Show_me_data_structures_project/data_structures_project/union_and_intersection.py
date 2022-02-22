
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    #for union we return a new linked list that contains all elemets in both llist_1 and llist_2
    intermediate_set = set()
    union_list = LinkedList()
    current_node1 = llist_1.head
    current_node2 = llist_2.head
    size1 = llist_1.size()
    size2 = llist_2.size()

    size = size1 if size1 > size2 else size2

    for i in range(size):
        if current_node1 != None:
            intermediate_set.add(current_node1.value)
            current_node1 = current_node1.next

        if current_node2 != None:
            intermediate_set.add(current_node2.value)
            current_node2 = current_node2.next


    for item in intermediate_set:
        union_list.append(item)

    return union_list

def intersection(llist_1, llist_2):
    #return a linked list containing elements both in llist_1 and llist_2
    current_node1 = llist_1.head
    current_node2 = llist_2.head
    intermediate_set = set()
    lis = set()
    size1 = llist_1.size()
    size2 = llist_2.size()
    intersection_list = LinkedList()
    
    size = size1 if size1 > size2 else size2

    #creating a set for the larger sized linked list

    for i in range(size):
        if size == size1:
            node = current_node1
            while node:
                lis.add(node.value)
                node = node.next
        else:
            node = current_node2
            while node:
                lis.add(node.value)
                node = node.next

    
    #comparing values in other linked list to see if in above created set therefore 
    #determining if an intersection has occured then adding the overlapping value in 
    #newly created output intersection list

    for i in range(size):
        if size == size1:
            if current_node2 !=None:
                if current_node2.value in lis:
                    intermediate_set.add(current_node2.value)
                current_node2 = current_node2.next
            

        else:
            if current_node1 !=None:
                if current_node1.value in lis: 
                    intermediate_set.add(current_node1.value)
                current_node1 = current_node1.next        
                


    for item in intermediate_set:
        intersection_list.append(item)

    

    return intersection_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

#expected output not in order
#6 -> 32 -> 4 -> 9 -> 6 -> 1 -> 11 -> 21 -> 3 -> 2 -> 35 -> 65 -> union
#6 -> 4 -> 21 -> intersection

# Test case 2 no intersection

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
# 1 -> 7 -> 8 -> 9 -> 11 ->21 -> 3 -> 2 -> 4 ->35 -> 6 -> 65 -> 23 -> union
# no intersection

#Test case no input completely
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_3 = [None for _ in range(10)]
element_4 = []

for i in element_3:
    linked_list_5.append(i)

for i in element_4:
    linked_list_6.append(i)

print(union(linked_list_5,linked_list_6))
print(intersection(linked_list_5,linked_list_6))

# None -> union
#no intersection


