# Implement Single Linked List in python using the following informations:
# Create class node with the members data and next. Develop a class
# Linkedlist with the following members:
# Data member start
# Define function __init__() to initialize the object of class LinkedList
# Define a function InsertBegining() to insert a new node in the beginning of
# the linked list
# Define a function InsertEnd() to insert at the end of the linked list
# Define a function InsertSpecified() to insert at specified position
# Define a function DeleteStart() to delete the start node
# Define a function DeleteEnd() to delete from the end.
# Define a function DeleteSpecified() to delete specified node
# Define a function traverse() to display all the data of the linked list.
# Define a function Reverse() to reverse the order of the nodes in the linked list
# Define a function Search() to search an element of the linked list

# Node class for a linked list
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to next node

# LinkedList class for managing operations
class LinkedList:
    def __init__(self):
        self.head = None  # Initially, no elements

    # Add at the beginning
    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Add at the end
    def add_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Add at a specific position (1-based index)
    def add_at(self, data, pos):
        if pos < 1:
            print("Invalid position!")
            return
        new_node = Node(data)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for _ in range(pos - 2):  # Move to (pos-1)th node
            if not temp:
                print("Position out of range")
                return
            temp = temp.next
        if temp:
            new_node.next = temp.next
            temp.next = new_node

    # Remove first node
    def remove_first(self):
        if self.head:
            self.head = self.head.next
        else:
            print("List is empty!")

    # Remove last node
    def remove_last(self):
        if not self.head:
            print("List is empty!")
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    # Remove at specific position
    def remove_at(self, pos):
        if not self.head:
            print("List is empty!")
            return
        if pos == 1:
            self.head = self.head.next
            return
        temp = self.head
        for _ in range(pos - 2):
            if not temp or not temp.next:
                print("Position out of range")
                return
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next

    # Display list elements
    def show(self):
        if not self.head:
            print("List is empty!")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Reverse the list
    def reverse(self):
        prev, current = None, self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Search for an element
    def search(self, key):
        temp, pos = self.head, 1
        while temp:
            if temp.data == key:
                print(f"Found {key} at position {pos}")
                return
            temp = temp.next
            pos += 1
        print(f"{key} not found in list")

# Testing the linked list
def main():
    ll = LinkedList()

    ll.add_first(10)
    ll.add_first(5)
    ll.add_last(20)
    ll.add_last(25)
    ll.add_at(15, 3)  # Insert 15 at position 3

    print("\nLinked List after insertions:")
    ll.show()

    ll.remove_first()
    print("\nAfter removing first node:")
    ll.show()

    ll.remove_last()
    print("\nAfter removing last node:")
    ll.show()

    ll.remove_at(2)
    print("\nAfter removing node at position 2:")
    ll.show()

    ll.reverse()
    print("\nAfter reversing the list:")
    ll.show()

    ll.search(10)
    ll.search(100)

# Running the main function
if __name__ == "__main__":
    main()