class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        return root

    def delete_node(self, root, data):
        if root is None:
            return root

        if data < root.data:
            print("Searching left subtree for", data)
            root.left = self.delete_node(root.left, data)
        elif data > root.data:
            print("Searching right subtree for", data)
            root.right = self.delete_node(root.right, data)
        else:  # Found the node!
            print("Deleting node with data:", data)
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.min_value(root.right)
            root.data = temp.data
            root.right = self.delete_node(root.right, temp.data)

        return root

    def min_value(self, node):
        while node.left is not None:
            node = node.left
        return node

# Create a tree and insert some nodes
my_tree = Tree()
root = None
root = my_tree.insert(root, 10)
my_tree.insert(root, 5)
my_tree.insert(root, 15)

# Example: Delete the node with value 5, 15, and 10 
root = my_tree.delete_node(root, 5) 
root = my_tree.delete_node(root, 15)
root = my_tree.delete_node(root, 10)
