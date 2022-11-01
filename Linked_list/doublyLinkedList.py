class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def traverseDoublyLinkedList(self):
        if self.head == None:
            print("No linked list to travel")

        else:
            temp = self.head
            while temp!=None:
                print(temp.value)
                temp = temp.next

    def insertAtStart(self, value):
        print(f"inserting {value} at start of linked list")
        if self.head == None:
            start = Node(value)
            self.head = start

        else:
            start = Node(value)
            self.head.prev = start
            start.next = self.head
            self.head = start

    def insertAtEnd(self, value):
        print(f"inserting {value} at end of linked list")
        if self.head == None:
            self.head = Node(value)

        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            
            newNode = Node(value)
            temp.next = newNode
            newNode.prev = temp

    def insertAtAnIndex(self, index, value):
        print(f"inserting: {value} at index: {index} of linked list")
        count = 0
        if self.head == None:
            self.head = Node(value)
        
        #if need to insert at 0th index
        elif (index == 0):
            self.insertAtStart(value)

        else:
            temp = self.head
            while (count<index and temp!=None):
                if (count == index-1):
                    #if end is none and temp reached index then insert at end
                    if temp.next == None:
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
            if temp == None:
                print(f"provided index doesn't exists so adding it at end")
                self.insertAtEnd(value)


    def deleteFromStart(self):
        print("deleting value from start")
        if self.head != None and self.head.next != None:
            start = self.head
            first = start.next
            first.prev = None
            self.head = first
            print(f"delete value {start.value} from start")
            del start

        elif self.head!=None and self.head.next == None:
            temp = self.head
            self.head = None
            del temp

        else:
            print("invalid linked list, cannot delete at start")

    def deleteFromEnd(self):
        print("deleting value from end")
        if self.head != None:
            first = self.head
            if (first.next == None):
                self.deleteFromStart()
            else:
                temp = first.next
                while(temp.next!=None):
                    temp = temp.next
                    first = first.next
                first.next = None
                print(f"delete value {temp.value} from end")
                del temp
        
    def deleteFromIndex(self, index):
        print(f"deleting node from an index {index}")

        if self.head == None:
            print(f"invalid linked list, cannot delete at index value: {index}")

        elif index == 0:
            self.deleteFromStart()
        
        elif index == 1:
            temp = self.head.next
            first = self.head
            second = temp.next
            second.prev = self.head
            first.next = second
            del temp
        
        else:
            count = 0
            temp = self.head
            while (count < index and temp!=None):
                if (count == index-1):
                    if temp.next == None:
                        print("error in deleting, None value")
                        break

                    else:
                        nodeToBeDeleted = temp.next 
                        temp.next = nodeToBeDeleted.next
                        temp.next.prev = temp
                        del nodeToBeDeleted
                        break

                else:
                    count += 1
                    temp = temp.next

if __name__ == "__main__":
    link = DoublyLinkedList()
    link.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    link.head.next = second
    second.prev = link.head
    second.next = third
    third.prev = second
    third.next = fourth
    fourth.prev = third

    link.insertAtStart(0)
    link.insertAtEnd(5)
    link.traverseDoublyLinkedList()

    link.insertAtAnIndex(4, -4)
    link.insertAtAnIndex(7, 6)
    link.traverseDoublyLinkedList()

    link.insertAtAnIndex(9, 8)
    link.traverseDoublyLinkedList()

    link.deleteFromEnd()
    link.deleteFromStart()
    link.deleteFromIndex(4)
    link.deleteFromIndex(1)
    link.traverseDoublyLinkedList()