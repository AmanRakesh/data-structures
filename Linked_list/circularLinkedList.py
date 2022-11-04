class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def traverseCircularLinkedList(self):
        start = self.head
        if start == None:
            print("No linked list to traverse")

        elif start.next == None:
            print(start.value)

        else:
            print(start.value)
            temp = start.next
            while temp != start:
                print(temp.value)
                temp = temp.next

    def insertAtEnd(self, value):
        print(f"inserting {value} at end of linked list")
        start = self.head

        if start == None:
            start = Node(value)

        else:
            temp = start
            while temp.next != start:
                temp = temp.next
            
            newNode = Node(value)
            newNode.next = start
            newNode.prev = temp
            temp.next = newNode

    
                
if __name__ == "__main__":
    link = CircularLinkedList()
    link.head = Node(1)
    start = link.head
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    

    start.next = second
    second.prev = start
    second.next = third
    third.prev = second
    third.next = fourth
    fourth.prev = third
    fourth.next = start
    start.prev = fourth

    link.traverseCircularLinkedList()

    link.insertAtEnd(5)
    link.traverseCircularLinkedList()
