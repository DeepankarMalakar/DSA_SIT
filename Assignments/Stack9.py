# Create an ADT for stack using OOPs concept.
# Define a class with the name Stack and with the following members
# Data member List l
# Data member Size of the array max
# Data membr top to identify top of the stack
# Define a member function(constructor) __init__ () which define an empty list l
# and define size of the list and initialize top with the value −1.
# Define member function Push(), to insert new element at the top of the stack.
# Modify top value accordingly.
# Define member function Traverse() to display all the values of the stack
# Define member function Pop() to remove an element from top of the stack. .
# Modify top value accordingly.

class Stack:
    def __init__(self, max_size):
        self.l = []  # Stack list
        self.max = max_size  # Stack size

    def push(self, value):
        if len(self.l) < self.max:
            self.l.append(value)
            print(f"Pushed {value}")
        else:
            print("Stack Overflow!")

    def pop(self):
        if self.l:
            print(f"Popped {self.l.pop()}")
        else:
            print("Stack Underflow!")

    def traverse(self):
        print("Stack:", self.l[::-1] if self.l else "Empty")

# Main function
def main():
    stack = Stack(int(input("Enter stack max size: ")))

    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.traverse()

    stack.pop()
    stack.traverse()

if __name__ == "__main__":
    main()