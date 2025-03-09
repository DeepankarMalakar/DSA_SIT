# Write a program to find the sum of the series 1 + 2 + 3 + 4 + 5 + ... + n where n is a positive integer.
def sum_series(n):
    return n * (n + 1) // 2  # Formula for sum of first n natural numbers

n = int(input("Enter a number: "))
print("Sum of series:", sum_series(n))
