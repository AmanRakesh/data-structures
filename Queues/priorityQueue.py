#linked list implementation of priority queue with making the descending order priority queue
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

    def enqueue(self, value, priority):
        print(f"enqueueing value: {value} with priority: {priority}")
        start = self.head
        end = self.tail

        if start == None:
            start = Node(value, priority)
            self.head = start
            self.tail = start
            self.size += 1

        elif start.next == None:
            temp = Node(value, priority)
            if (temp.value > start.value):
                temp.next = start
                self.head = temp
                self.tail = start
            
            else:
                start.next = temp
                self.tail = temp

        else:
            temp = Node(value, priority)
            if (start.value <= value):
                temp.next = start
                self.head = temp
            
            else:
                while (start.next.value > value and start.next != end):
                    start = start.next
                
                if (start.next != end):

                    if start.next.value < value:
                        temp = None(value, priority)
                        temp.next = start.next
                        start.next = temp
                



    def dequeue(self):
        print(f"dequeueing value: {self.tail.value} with priority: {self.tail.priority} from tail")
        start = self.head
        end = self.tail
        if start!=None:
            while (start.next!=end):
                start = start.next
            
            start.next = None
            del end

    def peek(self):
        return self.head.value

    def isEmpty(self):
        return True if self.head == None else False

    def size(self):
        return self.size

if __name__ == '__main__':
    self.head = Node(1)
    