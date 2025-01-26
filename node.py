class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

# Declaration of head Node initialized with None
class LinkedList:
    def __init__(self, head=None):
        self.head = head

    # Insert at the first position
    def insert_at_first(self, data):
        node = Node(data, self.head)
        node.next = self.head
        self.head = node

    # Print the elements of a linked list
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        else:
            itr = self.head
            while itr:
                print(itr.item, end=" ")
                itr = itr.next

# Test the LinkedList
l_list = LinkedList()
l_list.insert_at_first(5)
l_list.insert_at_first(89)
l_list.insert_at_first(79)

l_list.print()  # Output: 79 89 5