# Define a Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define the Linked List
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next   # Save next node
            current.next = prev        # Reverse pointer
