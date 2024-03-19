#write a python code to create a tree and then implement right rotate 

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def rightRotate(root):
    newRoot = root.left
    root.left = newRoot.right
    newRoot.right = root
    return newRoot

def inorderTraversal(root):
    if root is not None:
        inorderTraversal(root.left)
        print(root.data, end=' ')
        inorderTraversal(root.right)

def preorderTraversal(root):
    if root is not None:
        print(root.data, end=' ')
        preorderTraversal(root.left)
        preorderTraversal(root.right)

def postorderTraversal(root):
    if root is not None:
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        print(root.data, end=' ')

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print('Inorder Traversal:')
    inorderTraversal(root)
    print('\nPreorder Traversal:')
    preorderTraversal(root)
    print('\nPostorder Traversal:')
    postorderTraversal(root)

    root = rightRotate(root)

    print('\nInorder Traversal:')
    inorderTraversal(root)
    print('\nPreorder Traversal:')
    preorderTraversal(root)
    print('\nPostorder Traversal:')
    postorderTraversal(root)

    
