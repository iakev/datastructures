class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

def evaluate_post_fix(input_list):
    """
    Evaluate the postfix expression to find the answer

    Args:
       input_list(list): List containing the postfix expression
    Returns:
       int: Postfix expression solution
    """
    # operators = ('+','-','*','/')
    # operators_stack = Stack()
    # operand_stack = Stack()
    # # TODO: Iterate over elements 
    
    # # TODO: Use stacks to control the element positions

    # for i in range (0,len(input_list)+1):
    #     if operators_stack.size() == 1:
    #         if operators_stack.top() == '+':
    #             inter = int(operand_stack.pop())
    #             ans = int(operand_stack.pop()) + inter
    #             operators_stack.pop()
    #             operand_stack.push(ans)
                
    #         if operators_stack.top() == '*':
    #             inter = int(operand_stack.pop())
    #             ans = int(operand_stack.pop()) * inter
    #             operators_stack.pop()
    #             operand_stack.push(ans)
                
    #         if operators_stack.top() == '-':
    #             inter = int(operand_stack.pop())
    #             ans = int(operand_stack.pop()) - inter
    #             operators_stack.pop()
    #             operand_stack.push(ans)
                
    #         if operators_stack.top() == '/':
    #             inter = int(operand_stack.pop())
    #             ans = int(int(operand_stack.pop()) / inter)
    #             operators_stack.pop()
    #             operand_stack.push(ans)
                
    #     if  i < len(input_list) and input_list[i] in operators:
    #         operators_stack.push(input_list[i])
    #     elif i< len(input_list):
    #         operand_stack.push(input_list[i])
     
    # return ans
    stack = Stack()
    for element in input_list:
        if element == '*':
            second = stack.pop()
            first = stack.pop()
            output = first * second
            stack.push(output)
        elif element == '/':
            second = stack.pop()
            first = stack.pop()
            output = int(first / second)
            stack.push(output)
        elif element == '+':
            second = stack.pop()
            first = stack.pop()
            output = first + second
            stack.push(output)
        elif element == '-':
            second = stack.pop()
            first = stack.pop()
            output = first - second
            stack.push(output)
        else:
            stack.push(int(element))
    return stack.pop()





# evaluate_post_fix(["3", "1", "+", "4", "*"])

def test_function(test_case):
    output = evaluate_post_fix(test_case[0])
    print(output)
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")    
    
    
test_case_1 = [["3","1","+","4","*"], 16]
test_function(test_case_1)

test_case_2 = [["4", "13", "5", "/", "+"], 6]
test_function(test_case_2)

test_case_3 = [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22]
test_function(test_case_3)