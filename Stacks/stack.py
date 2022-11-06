class Node:

    def __init__(self, value):
        self.next = None
        self.value = value

class Stack:

    def __init__(self):
        head = None

    def push(self, value):
        start = self.head
        print(f"inserting value: {value} at top")
        if start == None:
            start = Node(value)
            self.head = start
        
        else:
            temp = Node(value)
            temp.next = start
            self.head = temp
    
    def pop(self):
        start = self.head
        if start == None:
            print("stack is empty, nothing to pop")
            return None

        print(f"poping the value: {start.value} from top")
        temp = start.next
        self.head = temp
        return start.value


    def top(self):
        print("returning top value from stack")
        return self.head.value

    def isEmpty(self):
        res = (self.head == None)
        print(f"checking if stack is empty: {res}")
        return res
        
            
if __name__ == "__main__":
    start = Stack()
    start.head = None
    start.isEmpty()
    start.push(1)
    start.push(2)
    start.push(3)
    start.push(4)
    start.push(5)
    print(start.top())
    print(start.pop())
    print(start.top())