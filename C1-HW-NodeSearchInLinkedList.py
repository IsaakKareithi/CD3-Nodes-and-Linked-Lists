# Define a node of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define the singly linked list
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert node at the end
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Search for a node
    def search(self, key):
        temp = self.head
        position = 1
        while temp:
            if temp.data == key:
                return position   # found, return position
            temp = temp.next
            position += 1
        return -1   # not found

# Example usage
if __name__ == "__main__":
    llist = LinkedList()

    # Create linked list: 10 -> 20 -> 30 -> 40
    llist.insert_end(10)
    llist.insert_end(20)
    llist.insert_end(30)
    llist.insert_end(40)

    key = int(input("Enter value to search: "))
    result = llist.search(key)

    if result != -1:
        print(f"Element {key} found at position {result}.")
    else:
        print(f"Element {key} not found in the list.")
