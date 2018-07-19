class Queue (object):
    def __init__(self):
        pass


# What are characteristics of a stack?
# it needs a tail
# it needs a head
# anything added goes to the back of the line(tail)
# anything removed is taken from the front (head)

class Node(object):
    def __init__(self):
        self.value = None
        self.next = None

class linked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def enqueue(node):
        node.next = self.tail
        self.tail = node
    def dequeue():
        self.head = self.head.next
        
a = linked_list()