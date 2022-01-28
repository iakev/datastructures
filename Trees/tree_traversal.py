"""
Contains definitions for node,tree
definitions for stack, state which help in tree traversal
contains routines for tree traversal i.e DFS-> pre-order
"""

class Node(object):
        
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None
        
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
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"


class State:
    def __init__(self,node):
        self.node = node
        self.visited_left = False
        self.visited_right = False

    def get_node(self):
        return self.node

    def get_visited_left(self):
        return self.visited_left

    def get_visited_right(self):
        return self.visited_right

    def set_visited_left(self):
        self.visited_left = True    
    
    def set_visited_right(self):
        self.visited_right = True

    def __repr__(self):
        s = f"""{self.node}
visited_left: {self.visited_left}
visited_right: {self.visited_right}        
        """
        return s

class Tree:
    def __init__(self, value=None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root

#defining a stack to help us travesr the tree above
class Stack:
    def __init__(self):
        self.list = list()

    def push(self,value):
        self.list.append(value)

    def pop (self):
        return self.list.pop()

    def top(self):
        if len(self.list) > 0:
            return self.list[-1]

        else:
            return None

    def is_empty(self):
        return len(self.list) == 0

    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_______________\n"
            s += "\n_______________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_______________\n<bottom of stack>"
            return s
        else:
            return "<stack is empty>"


#creating a tree and some node

tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))


# check stack
# stack  = Stack()
# stack.push("apple")
# stack.push("banana")
# stack.push("cherry")
# stack.push("dates")

###################################################################################################
###################################################################################################
# visit_order = list()
# stack = Stack()

# #start at root node, visit it and add it to the stack
# node = tree.get_root()
# stack.push(node)

# print(f"""
# visit_order {visit_order}
# stack:
# {stack}
# """)

# #visit apple
# visit_order.append(node.get_value())
# print(f"""visit_order {visit_order}""")

# # check if apple has a left child
# print(f"{node} has a left child? {node.has_left_child()}")

# if node.has_left_child():
#     node = node.get_left_child()
#     stack.push(node)

# print(f"""
# visit_order {visit_order}
# stack:
# {stack}
# """)

# #visit banana
# print(f"visit {node}")
# visit_order.append(node.get_value())
# print(f"""visit_order {visit_order}""")

# # check if banana has a left node
# print(f"{node} has a left child? {node.get_left_child()}")

# if node.has_left_child():
#     node = node.get_left_child()
#     stack.push(node)

# print(f"""
# visit_order {visit_order}
# stack:
# {stack}
# """)

# #visit dates
# print(f"visit {node}")
# visit_order.append(node.get_value())
# print(f"""visit_order {visit_order}""")

# # check if dates has a left child
# print(f"{node} has a left child? {node.get_left_child()}")

# # check if dates has a rigth child
# print(f"{node} has a left child? {node.get_right_child()}")

# #since no left/right child its a leaf
# stack.pop()

# print(stack)

# # now we'll set the node to the new top of the stack, which is banana
# node = stack.top()
# print(node)

# # we already checked for banana's left child, so we'll check for its right child
# print(f"{node} has right child? {node.has_right_child()}")

# print(f"pop {stack.pop()} off stack")
# print(f"""
# stack
# {stack}
# """)

# # now we'll track the new top of the stack, which is apple
# node = stack.top()
# print(node)

# # we've already checked if apple has a left child; we'll check if it has a right child
# print(f"{node} has right child? {node.has_right_child()}")

# # since it has a right child (cherry), 
# # we'll visit cherry and add it to the stack.
# if node.has_right_child():
#     node = node.get_right_child()
#     stack.push(node)
    
# print(f"""
# visit_order {visit_order} 
# stack
# {stack}
# """)

# # visit cherry
# print(f"visit {node}")
# visit_order.append(node.get_value())
# print(f"""visit_order: {visit_order}""")

# # Now we'll check if cherry has a left child
# print(f"{node} has left child? {node.has_left_child()}")

# # it doesn't, so we'll check if it has a right child
# print(f"{node} has right child? {node.has_right_child()}")

# # since cherry has neither left nor right child nodes,
# # we are done tracking it, and can pop it off the stack

# print(f"pop {stack.pop()} off the stack")

# print(f"""
# visit_order {visit_order} 
# stack
# {stack}
# """)

# # now we're back to apple at the top of the stack.
# # since we've already checked apple's left and right child nodes,
# # we can pop apple off the stack

# print(f"pop {stack.pop()} off stack")
# print(f"pre-order traversal visited nodes in this order: {visit_order}")

# print(f"""stack
# {stack}""")
###################################################################################################################################
###########################################################################################################################

# Turning above traversal section enclosed by pound(hashtag) signs to a function

def pre_order_with_stack(tree, debug_mode=False):
    visit_order = list()
    stack  = Stack()
    node = tree.get_root()
    visit_order.append(node.get_value())
    state = State(node)
    stack.push(state)
    count = 0

    while(node):
        if debug_mode:
            print(f"""
loop count: {count}
current node: {node}
stack:
{stack}      
            """)
            count+=1
            if node.has_left_child() and not state.get_visited_left():
                state.set_visited_left()
                node = node.get_left_child()
                visit_order.append(node.get_value())
                state = State(node)
                stack.push(state)

            elif node.has_right_child() and not state.get_visited_right():
                state.set_visited_right()
                node = node.get_right_child()
                visit_order.append(node.get_value())
                state = State(node)

            else:
                stack.pop()
                if not stack.is_empty():
                    state = stack.top()
                    node = state.get_node()

                else:
                    node = None

    if debug_mode:
        print(f"""
loop count: {count}
current node: {node}
stack:
{stack}
        """)

    return visit_order

# pre_order_with_stack(tree,True)


#############################################################################################
# Implement above function DFS pre-order via recursion 
#############################################################################################

def pre_order1(tree):
    visit_order = list()
    node = tree.get_root()
    stack = Stack()
    state = State(node)
    stack.push(state)
    visit_order.append(node.value)
    
    recursive_traverse(stack,visit_order)
    
    return visit_order


def recursive_traverse(stack,visit_order):
    if stack != None:
        state = stack.top()
        # base case defined
        if state == None:
            return    
        node = state.get_node()

    
        if node.has_left_child() and not  state.get_visited_left():
            state.set_visited_left()
            node = node.get_left_child()
            state = State(node)
            stack.push(state)
            value = node.value
            visit_order.append(value) 

        elif node.has_right_child() and not  state.get_visited_right():
            state.set_visited_right()
            node = node.get_right_child()
            state = State(node)
            value = node.value
            visit_order.append(value)

        else:
            stack.pop()
            value = None
            if stack.is_empty():
                node = None
                stack = None

        recursive_traverse(stack,visit_order)
        return 

# pre_order1(tree)

##########################################################################################################################
# Tree traversal utilising recurion UDACITY solution
##########################################################################################################################
def  pre_order(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):
        if node:
            #visit
            visit_order.append(node.value)
            #traverse left
            traverse(node.get_left_child())

            #traverse right
            traverse(node.get_right_child())
    
    traverse(root)

    return visit_order

pre_order(tree)