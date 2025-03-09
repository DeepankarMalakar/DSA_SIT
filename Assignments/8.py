# Create an ADT of array using OOPs concept.
# Define a class with the name 𝑎𝑟𝑟𝑎𝑦1 and with the following members
# Data member List 𝑙
# Data member Size of the array 𝑚𝑎𝑥
# Define a member function(constructor) __𝑖𝑛𝑖𝑡__ () which define an empty list 𝑙
# and define size of the list.
# Define member function 𝐶𝑟𝑒𝑎𝑡𝑒𝐴𝑟𝑟𝑎𝑦(), take input for the list 𝑙 with size 𝑚𝑎𝑥
# Define member function 𝑆ℎ𝑜𝑤𝐴𝑟𝑟𝑎𝑦() display all the values of the array
# Define member function 𝐿𝑖𝑛𝑒𝑎𝑟𝑆𝑒𝑎𝑟𝑐ℎ(), search one item in the array, return
# index of the item
# Define member function 𝑆𝑜𝑟𝑡𝑖𝑛𝑔(), arrange all the elements in sorted order
# Define member function 𝐵𝑖𝑛𝑎𝑟𝑦𝑆𝑒𝑎𝑟𝑐ℎ(), return index of the item in the
# sorted array
# Write a main function, create an object of the class 𝑎𝑟𝑟𝑎𝑦1, call all the
# member functions of the class 𝑎𝑟𝑟𝑎𝑦1 and implements data structure
# operations on array.

class SimpleArray:
    def __init__(self, size):
        self.l = []
        self.size = size

    def create_array(self):
        print("Enter", self.size, "numbers:")
        for _ in range(self.size):
            num = int(input("Enter a number: "))
            self.l.append(num)

    def show_array(self):
        print("Array elements:", self.l)

    def linear_search(self, key):
        for i in range(len(self.l)):
            if self.l[i] == key:
                return i
        return -1

    def sort_array(self):
        self.l.sort()
        print("Sorted Array:", self.l)

    def binary_search(self, key):
        low, high = 0, len(self.l) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.l[mid] == key:
                return mid
            elif self.l[mid] < key:
                low = mid + 1
            else:
                high = mid - 1
        return -1

# Main function to test
def main():
    size = int(input("Enter the size of the array: "))
    arr = SimpleArray(size)

    arr.create_array()
    arr.show_array()

    key = int(input("Enter number to search (Linear Search): "))
    index = arr.linear_search(key)
    print(f"Element found at index: {index}" if index != -1 else "Element not found")

    arr.sort_array()

    key = int(input("Enter number to search (Binary Search): "))
    index = arr.binary_search(key)
    print(f"Element found at index: {index}" if index != -1 else "Element not found")

if __name__ == "__main__":
    main()
