class BinaryTrees:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorderTraversal(temp):
    if temp == None:
        return
        
    inorderTraversal(temp.left)
    print(temp.value)
    inorderTraversal(temp.right)


