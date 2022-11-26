class BinaryTrees:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



# Binary Tree Traversals:
# Tree Traversal algorithms can be classified broadly into two categories:

# Depth-First Search (DFS) Algorithms
# Breadth-First Search (BFS) Algorithms


# below are dfs traversal methods
def inorderTraversal(temp):
    if temp == None:
        return
        
    inorderTraversal(temp.left)
    print(temp.value)
    inorderTraversal(temp.right)


def preorderTraversal(temp):

    if temp == None:
        return

    print(temp.value)
    inorderTraversal(temp.left)
    inorderTraversal(temp.right)

def postOrderTraversal(temp):
    
    if temp == None:
        return

    inorderTraversal(temp.left)
    inorderTraversal(temp.right)
    print(temp.value)

    



