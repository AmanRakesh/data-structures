#linked list implementation of priority queue
class Node:

    def __init__(self, value, priority):
        self.next = None
        self.value = value
        self.priority = priority

class PriorityQueue:

    def __init__(self):
        head = None
        tail = None
        size = 0

    def enqueue(self):
        pass

    def dequeue(self):
        pass

    def peek(self):
        return self.head.value

    def isEmpty(self):
        return True if self.head == None else False

        