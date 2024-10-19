from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete(self, key):
        current = self.head

        # If the head node itself holds the key to be deleted
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Search for the key to be deleted, keep track of the previous node
        previous = None
        while current and current.data != key:
            previous = current
            current = current.next

        # If the key was not present in the linked list
        if not current:
            return

        # Unlink the node from the linked list
        previous.next = current.next
        current = None

ll = LinkedList()
# Append some elements
ll.append(1)
ll.append(2)
ll.append(3)

# Display the linked list
ll.display()  # Output: 1 -> 2 -> 3 -> None

# Delete an element
ll.delete(2)

# Display the linked list again
ll.display() 
