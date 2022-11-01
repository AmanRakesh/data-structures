class Node:

    def __init__(self, value):
        self.next = None
        self.value = value

class LinkedList:

    def __init__(self):
        head = None

    def traverseLinkedList(self):
        print("traversing the linked list")
        if self.head != None:
            temp = self.head

            while temp:
                print(temp.value)
                temp = temp.next
        else:
            print("No linkedList to traverse")

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


    def insertAtStart(self, value):
        print(f"inserting {value} at start of linked list")
        if self.head == None:
            self.head = Node(value)

        else:
            temp = Node(value)
            temp.next = self.head
            self.head = temp


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
            head = self.head
            self.head = head.next
            print(f"delete value {head.value} from start")
            del head

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
            first.next = temp.next
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
                        del nodeToBeDeleted
                        break

                else:
                    count += 1
                    temp = temp.next

    def reverseTheLinkedList(self):
        print("reversing a linked list")
        start = self.head
        temp = start.next
        start.next = None
        thirdTemp = None

        while temp != None:
            secondTemp = temp

            if (thirdTemp == None):
                temp = temp.next
                secondTemp.next = start
                thirdTemp = secondTemp

            else:
                temp = temp.next
                secondTemp.next = thirdTemp
                thirdTemp = secondTemp


        self.head = thirdTemp




if __name__ == "__main__":
    link = LinkedList()
    link.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    link.head.next = second
    second.next = third
    third.next = fourth
    link.insertAtStart(0)
    link.insertAtEnd(5)
    link.insertAtAnIndex(0, -1)
    link.insertAtAnIndex(7, 7)
    link.insertAtAnIndex(7,6)
    link.traverseLinkedList()

    link.deleteFromStart()
    link.traverseLinkedList()

    link.deleteFromEnd()
    link.traverseLinkedList()

    link.deleteFromIndex(1)
    link.traverseLinkedList()

    link.reverseTheLinkedList()
    link.traverseLinkedList()

