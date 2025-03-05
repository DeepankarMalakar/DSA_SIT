class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, data):
        self.stack.append(data)
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return 'Stack is empty'
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        return None
    def isEmpty(self):
        return len(self.stack) == 0

# Test the Stack class
stack = Stack()

stack.push(10)
stack.push(40)
stack.push(5)
stack.push(30)

print(stack.stack)    # [10, 40, 5, 30]
print("Peek:", stack.peek())   #30

print("Pop:", stack.pop())  # 30
print("Peek after pop:", stack.peek()) # 5

print("Push:", stack.push(100))
print("After pushing:", stack.stack) # [10, 40, 5, 100]