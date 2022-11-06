class Node:

    def __init__(self, value):
        self.next = None
        self.value = value

class Queue:

    def __init__(self):
        head = None
        tail = None
        size = 0

    def isEmpty(self):
        if self.head == None:
            print("Queue is empty")
            return True
        else:
            return False
    
    def push(self, value):
        print(f"pushing {value} at front of queue")
        if self.head == None:
            temp = Node(value)
            self.head = temp
            self.tail = temp
        
        else:
            temp = Node(value)
            temp.next = self.head
            self.head = temp
    
    def pop(self):
        if (self.tail != None):
            print(f"popping value: {self.tail.value} from end")
            temp = self.tail
            start = self.head

            while start.next!=temp:
                start = start.next
            
            self.tail = start
            start.next = None
            del temp
        else:
            print("queue looks to be empty")

    def front(self):
        if self.head != None:
            print(f"front of queue: {self.head.value}")
            return self.head.value

        else:
            print("Queue empty")

    def back(self):
        if self.tail!= None:
            print(f"back of queue: {self.head.value}")
            return self.tail.value

        else:
            print("Queue empty")

    def size(self):
        if self.head != None:
            pass
        else:
            return self


if __name__ == "__main__":
    start = Queue()

    start.push(1)
    start.push(2)
    start.push(3)
    start.push(4)
    start.push(5)

    start.front()
    start.back()
    start.pop()
    start.isEmpty()
    start.back()
