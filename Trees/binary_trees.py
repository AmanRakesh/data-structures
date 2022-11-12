class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinaryTrees:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root == Node(value)

        else:
            root = self.root
            
            #value is less hence adding in left
            if root.value <= value:
                temp = root.left
                if temp == None:
                    temp = Node(value)
                    root.left = temp
                
                else:
                    self.insert()
