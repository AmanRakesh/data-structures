class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
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

    def insertAtStart(self, value):
        print(f"inserting {value} at start of linked list")
        if self.head == None:
            start = Node(value)
            self.head = start

        else:
            start = self.head
            temp = Node(value)
            temp.next = start
            temp.prev = start.prev
            temp.prev.next = temp
            start.prev = temp
            self.head = temp

    def insertAtEnd(self, value):
        print(f"inserting {value} at end of linked list")
        start = self.head

        if start == None:
            start = Node(value)

        else:
            temp = start.prev
            newNode = Node(value)
            newNode.next = start
            newNode.prev = temp
            temp.next = newNode
            start.prev = newNode

    def insertAtAnIndex(self, index, value):
        print(f"inserting: {value} at index: {index} of linked list")
        start = self.head
        count = 1
        if self.head == None:
            self.head = Node(value)
        
        #if need to insert at 0th index
        elif (index == 0):
            self.insertAtStart(value)
        
        elif index == 1:
            temp = start.next
            newTemp = Node(value)
            newTemp.next = temp
            newTemp.prev = start
            start.next = newTemp
            temp.prev = newTemp

        else:
            temp = start.next
            while (count<index and temp!=start):
                if (count == index-1):
                    #if end is none and temp reached index then insert at end
                    if temp.next == start:
                        self.insertAtEnd(value)
                        break
                    
                    #else insert it normally
                    else:
                        indexedNode = temp.next
                        newTemp = Node(value)
                        newTemp.next = indexedNode
                        indexedNode.prev = newTemp
                        newTemp.prev = temp
                        temp.next = newTemp
                        break
                else:
                    count += 1
                    temp = temp.next

            #handling for some outward index, in case at the temp reached end of linkedlist
            if temp == start:
                print(f"provided index doesn't exists so adding it at end")
                self.insertAtEnd(value)
    
    def deleteFromStart(self):
        print("deleting value from start")
        start = self.head
        if start == None:
            print("Nothing to delete")
        
        elif start.next == None:
            start = self.head
            self.head = None
            del start
        
        else:
            end = start.prev
            temp = start.next
            end.next = temp
            temp.prev = end
            self.head = temp
            print(f"deleted value: {start.value} from linked list")
            del start

    def deleteFromEnd(self):
        print("deleting value from end")
        start = self.head
        if start != None:
            if (start.next == None):
                self.deleteFromStart()

            else:
                nodeToDelete = start.prev
                if nodeToDelete.prev != start:
                    temp = nodeToDelete.prev
                    temp.next = start
                    start.prev = temp
                    print(f"delete value {nodeToDelete.value} from end")
                    del nodeToDelete

                else:
                    temp = start.prev
                    start.prev = None
                    start.next = None
                    del temp

        else:
            print("Nothing to delete")

                
if __name__ == "__main__":
    link = CircularDoublyLinkedList()
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

    link.insertAtStart(0)
    link.insertAtStart(-1)
    link.insertAtEnd(5)
    link.insertAtAnIndex(2, 0.5)
    link.insertAtAnIndex(12, 10)
    link.traverseCircularLinkedList()

    link.deleteFromStart()
    link.traverseCircularLinkedList()
    link.deleteFromEnd()
    link.traverseCircularLinkedList()