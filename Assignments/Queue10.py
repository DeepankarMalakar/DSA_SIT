# Create an ADT for Queue using OOPs concept(Imagine Python list do not
# support append and pop).
# Define a class with the name Queue and with the following members
# Data member List l
# Data member Size of the array max
# Data member front and rear
# Define a member function(constructor) __init__ () which define a list l with the
# entries zeros of size max and initialize front and rear with the value −1.
# Define member function Insertion(), to insert new element at the top of the
# rear.
# Define member function Traverse() to display all the values of the queue
# Define member function Deletion() to remove an element from front of the
# queue.

class Queue:
    def __init__(self, max_size):
        self.l = [0] * max_size  # Initialize a list with zeros
        self.max = max_size  # Maximum size of the queue
        self.front = -1  # Initialize front pointer
        self.rear = -1  # Initialize rear pointer

    def Insertion(self, value):
        if self.rear == self.max - 1:  # Check if queue is full
            print("Queue Overflow! Cannot insert more elements.")
        else:
            if self.front == -1:  # If queue is empty, move front to 0
                self.front = 0
            self.rear += 1
            self.l[self.rear] = value  # Insert at the rear
            print(f"Inserted {value} into queue")

    def Traverse(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is empty.")
        else:
            print("Queue elements:", self.l[self.front:self.rear + 1])

    def Deletion(self):
        if self.front == -1 or self.front > self.rear:  # Check if queue is empty
            print("Queue Underflow! Cannot delete from an empty queue.")
        else:
            print(f"Deleted {self.l[self.front]} from queue")
            self.front += 1  # Move front forward
            if self.front > self.rear:  # Reset when queue becomes empty
                self.front = self.rear = -1

# Main function
def main():
    size = int(input("Enter queue size: "))
    queue = Queue(size)

    queue.Insertion(10)
    queue.Insertion(20)
    queue.Insertion(30)
    queue.Traverse()  # Show queue elements

    queue.Deletion()
    queue.Traverse()  # Show queue after deletion

# Running the main function
if __name__ == "__main__":
    main()