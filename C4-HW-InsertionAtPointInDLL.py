class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLL:
    def __init__(self):
        self.head = None
    
    #Insert element at a apecific position
    def insertAtPos(self, data, position):
        ne = Node(data)

        if position == 1:
            ne.next = self.head
            if self.head:
                self.head.prev = ne
            self.head = ne
            return
        temp = self.head
        count = 1

        #traverse to the position 
        while temp and count < position - 1:
            temp = temp.next 
            count += 1

        if not temp:
            print("Position is out of range!")
            return
        
        # Insert in between or at the end 
        ne.next = temp.next 
        ne.prev = temp

        if temp.next:
            temp.next.prev = ne 
        temp.next = ne 

    # Function to print the list 
    def display(self):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=' ')
                temp = temp.next 

#driver code 
l = DoublyLL()
l.insertAtPos(10, 1)
l.insertAtPos(20, 2)
l.insertAtPos(30, 3)
l.insertAtPos(15, 2)

l.display()