# Node class for Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Function to add a node at the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:  # If list is empty
            self.head = new_node
            return
        temp = self.head
        while temp.next:  # Traverse to last node
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    # Function to insert at a specific position (1-based index)
    def insert_at_position(self, data, position):
        new_node = Node(data)

        # Case 1: Insert at the head
        if position == 1:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        temp = self.head
        count = 1
        while temp and count < position - 1:
            temp = temp.next
            count += 1

        # If position is beyond length, insert at end
        if temp is None:
            print("Position out of range, inserting at end.")
            self.append(data)
            return

        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node

    # Function to display the list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next
        print("None")


# Example usage
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)

print("Original List:")
dll.display()

dll.insert_at_position(5, 1)   # Insert at head
dll.insert_at_position(25, 3)  # Insert in middle
dll.insert_at_position(40, 10) # Insert beyond range (at end)

print("\nList after insertions:")
dll.display()
