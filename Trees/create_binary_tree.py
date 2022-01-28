## Define a node
## your code here
class Node(object):
    def __init__(self,value=None):
        self.value = value
        self.left = None #pointer to next left node in tree
        self.right = None #pointer to next right node in tree
    
    def get_value(self):
        return self.value
    
    def set_value(self,value):
        self.value = value
        
    def set_left_child(self,node):
        self.left = node
        
    def set_right_child(self,node):
        self.right = node
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right
    
    def has_left_child(self):
        return self.get_left_child() != None

    def has_right_child(self):
        return self.get_right_child() != None


#Creating a binary Tree
class Tree(object):
    def __init__(self,value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root 


