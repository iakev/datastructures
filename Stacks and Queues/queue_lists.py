class Queue:
    def __init__(self):
         # TODO: Initialize the Queue
         self.head = None
         self.tail = None
         self.ls = []
    
    def size(self):
         # TODO: Check the size of the Queue
         return len(self.ls)
    
    def enqueue(self, item):
         # TODO: Enter item into Queue
         if self.size() == 0:
            self.ls.append(item)
            self.head = 0
            self.tail = self.head
         else:
            self.ls.append(item)
            self.tail += 1  

    def dequeue(self):
         # TODO: Remove item from the Queue
        if self.size == 0:
            return None
        
        popped = self.ls.pop(self.head)
        # self.head += 1
        return popped


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.size()
q.dequeue()
q.enqueue(4)
q.dequeue()
q.dequeue()
q.dequeue()