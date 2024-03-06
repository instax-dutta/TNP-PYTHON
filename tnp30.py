class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insertion methods

    def push(self, new_data):
        """Inserts a new node at the beginning"""
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        """Inserts a new node after the given previous node"""
        if prev_node is None:
            print("Previous node cannot be None")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        """Inserts a new node at the end"""
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Deletion method

    def delete_node(self, key):
        """Deletes the node with the given key"""
        temp = self.head

        # If the key is in the head node
        if temp and temp.data == key:
            self.head = temp.next
            temp = None  # Facilitate garbage collection
            return

        # Search for the key in other nodes
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:  # Key not found
            return

        prev.next = temp.next
        temp = None  # Facilitate garbage collection

    # Utility methods

    def print_list(self):
        """Prints the contents of the linked list"""
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def get_length(self):
        """Returns the length (count) of nodes in the list"""
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

# Example usage
if __name__ == '__main__':
    llist = LinkedList()
    llist.append(1)
    llist.push(2)
    llist.append(3)
    llist.insert_after(llist.head.next, 8)

    print('Created linked list:')
    llist.print_list()

    llist.delete_node(8)
    print("\nLinked list after deletion:")
    llist.print_list()

    print("\nLength of the linked list:", llist.get_length())
