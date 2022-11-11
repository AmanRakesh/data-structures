#linked list implementation of priority queue with making the ascending order priority queue
class Node:

    def __init__(self, value, priority):
        self.next = None
        self.value = value
        self.priority = priority

class PriorityQueue:

    def __init__(self):
        head = None
        tail = None

    def enqueue(self, value, priority):
        print(f"enqueueing value: {value} with priority: {priority}")
        start = self.head
        end = self.tail

        if start == None:
            start = Node(value, priority)
            self.head = start
            self.tail = start

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
                        temp = Node(value, priority)
                        temp.next = start.next
                        start.next = temp

                else:
                    temp = Node(value, priority)
                    start.next = temp
                    self.tail = temp




    def dequeue(self):
        start = self.head
        end = self.tail
        print(f"dequeueing value: {end.value} with priority: {end.priority} from tail")
        if start!=None:
            while (start.next!=end):
                start = start.next
            
            start.next = None
            del end

    def peek(self):
        return self.tail.value

    def isEmpty(self):
        return True if self.head == None else False

    def size(self):
        start = self.head
        end = self.tail
        count = 0
        while start!=end:
            count = count + 1
            start = start.next

        return count

if __name__ == '__main__':
    queue = PriorityQueue()
    queue.head = None
    queue.tail = None
    queue.enqueue(0,1)
    queue.enqueue(1,2)
    queue.enqueue(2,1.5)
    queue.enqueue(3,3)
    queue.enqueue(4,2.5)
    queue.enqueue(5, 5)
    print(queue.peek())
    print(queue.size())

    queue.dequeue()
    print(queue.peek())
    
    
    