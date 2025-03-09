# The queue implementation defined in the last question does not utilize the
# storage space effectively. This issues leads to circular queue, implement
# circular queue with the required operations.

class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full! Cannot insert more elements.")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        print(f"Inserted {value} into queue")

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty! Cannot delete.")
            return

        print(f"Deleted {self.queue[self.front]} from queue")

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    def display(self):
        if self.front == -1:
            print("Queue is empty.")
            return

        print("Queue elements:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

def main():
    size = int(input("Enter the circular queue size: "))
    cq = CircularQueue(size)

    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    cq.display()

    cq.dequeue()
    cq.display()

if __name__ == "__main__":
    main()