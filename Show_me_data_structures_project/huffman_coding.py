
# %%
class Node:
        
    def __init__(self,key = None,value = None):
        self.root = None
        self.key = key
        self.value = value
        self.left = None #left_child
        self.right = None #right_child
        self.bit = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None

    def set_bit(self,value):
        self.bit = value

    def get_bit(self):
        return self.bit

class Minheap:
    
    #creating a min_heap to simulate a priority queue
    def __init__(self,value=None):
        self.arr = []

    ##common operations are:
    # Find minimum which is the root node (peek)
    #operation without modifying the heap
    def find_min(self):
        return self.arr[0]

    #insert a new key to the heap
    #NB: need to maintain heap property during insertion
    def push(self,key=None,value=None,node=None):
        """
        Accepts either a key-value pair,
        or a Node object.
        """
        if key != None and value != None:
            new_node = Node(key,value)

        else:
            new_node = node
        
        #insert at the end of the heap first
        self.arr.append(new_node)
        #if heap property is violated implement sift up operation to restore heap operation
        for i in range(len(self.arr)-1,-1,-1): #starting from the back of the array so as to do a sift up operation
            if new_node.value < self.arr[i].value:
                child = self.arr[i]
                self.arr[i] = new_node
                self.arr[i+1] = child

    
    def pop(self):
        #remember the removal is for the minimum value i.e root in this case.
        if len(self.arr) != 0:
            return self.arr.pop(0)
        return 
    # return number of elements in heap
    def size(self):
        return len(self.arr)

    # return true if heap is empty or false otherwise    
    def is_empty(self):
        if len(self.arr) == 0:
            return True
        return False



import sys

def det_frequency(message):
    freq_map = {} #create a dictionary to hold chatacters and their respective counts
    
    for char in message:
        if char not in freq_map: #initializing frequency count
            freq_map[char] = 1 
        else:
            freq_map[char] += 1 #increase count depending on occurences
    return freq_map

def generate_code(tree):

    encoded_dict = {} #mapping character to respective binary code

    str_code = "" #string to store the binary code

    generate_code_recursively(tree,encoded_dict,str_code)

    return encoded_dict

def generate_code_recursively(huffmantree,code_dict,str_code):
    node = huffmantree
    # base case
    if not node.has_left_child() and not node.has_right_child():
        code_dict[node.key] = str_code 
        return
    #recursive cases
    else:
        if node.has_left_child() and node.has_right_child(): #node is internal in huffman tree
            str_code += str(node.left.get_bit())
            generate_code_recursively(node.left,code_dict,str_code)
            str_code = str_code[0:len(str_code)-1]
            str_code += str(node.right.get_bit())
            generate_code_recursively(node.right,code_dict,str_code)

def huffman_encoding(data):

    try:
        if data == "":
            raise ValueError
        encoded_data = ""
        #Determining freuency of message string characters:
        freq_dict = det_frequency(data)
        ## Building a priority queue:##
        min_heap  = Minheap()
        
        #constructing a min_heap priority queue from frequency dictionary items
        for key,value in freq_dict.items():  
            min_heap.push(key,value)
        
        # while loop to build the huffman tree
        while len(min_heap.arr) != 1:
            #popping first two nodes from the priority queue and assigning bit codes
            first_node = min_heap.pop()
            first_node.set_bit(0)
            second_node = min_heap.pop()
            second_node.set_bit(1)
            #creating a new_node with frequency equal to sums of the above two nodes values
            sum_nodes = first_node.value + second_node.value
            internal_node = Node(str(sum_nodes),sum_nodes)
            internal_node.left = first_node
            internal_node.right = second_node
            #newly created internal_node to be inserted back to priority queue again
            min_heap.push(node=internal_node)

        #traversing the huffman_tree from root to node to generate encoded data
        tree = min_heap.arr[0] #reference to huffman tree node
        #traversing the huffman_tree from root to node to generate encoded data dictionary
        encoded_dict = generate_code(tree)
        # generating encoded data
        for key in data: 
            encoded_data += str(encoded_dict[key])

        return encoded_data,tree
        
    except ValueError:
        print("Ooops!  Can't encode an empty string")


def huffman_decoding(data,tree):
    decoded_message = ""
    node = tree
    for bit in data:
        if bit == '1':
            node = node.right
        if bit == '0':
            node = node.left

        if not node.has_left_child() and not node.has_right_child(): # if leaf node
            decoded_message += node.key
            node = tree
            continue

    return decoded_message

if __name__ == "__main__":
    codes = {}

    try:
        # Test 1

        a_great_sentence = "The bird is the word"

        print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        # returns The size of the data is: 69
        
        print ("The content of the data is: {}\n".format(a_great_sentence))
        # returns The content of the data is: The bird is the word

        encoded_data, tree = huffman_encoding(a_great_sentence)

        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        # returns The size of the encoded data is: 36

        print ("The content of the encoded data is: {}\n".format(encoded_data))
        # returns The content of the encoded data is: 0110111011111100111000001010110000100011010011110111111010101011001010

        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        #returns The size of the decoded data is: 69

        print ("The content of the decoded data is: {}\n".format(decoded_data))
        #returns The content of the decoded data is: The bird is the word

        # Test 2

        a_greater_sentence = "God is good all the time."

        print ("The size of the data is: {}\n".format(sys.getsizeof(a_greater_sentence)))
        # returns The size of the data is: 74

        print ("The content of the data is: {}\n".format(a_greater_sentence))
        # returns The content of the data is: God is good all the time.
        
        encoded_data, tree = huffman_encoding(a_greater_sentence)

        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        # returns The size of the encoded data is: 40
        
        print ("The content of the encoded data is: {}\n".format(encoded_data))
        # returns The content of the encoded data is: 1110001110010010101110100111100110111001001111110111011001100010011010011001010010111011000
        
        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        # returns The size of the decoded data is: 74
        
        print ("The content of the decoded data is: {}\n".format(decoded_data))
        # returns The content of the decoded data is: God is good all the time.
        
        # Test 3

        an_empty_sentence = ""

        print ("The size of the data is: {}\n".format(sys.getsizeof(an_empty_sentence)))
        # returns The size of the data is: 49

        print ("The content of the data is: {}\n".format(an_empty_sentence))
        # returns The content of the data is:
        
        encoded_data, tree = huffman_encoding(an_empty_sentence)
        #raises a value error exception and a type error exception as well

        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))

        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))

        print ("The content of the decoded data is: {}\n".format(decoded_data))
    except TypeError:
        print("Can't unpack invalid output due to invalid encoding data")
# %%
