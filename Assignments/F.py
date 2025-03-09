# F. Write a function thant takes a list of integers as a parameters and
# returns third smallest number from the list. For example,
# input:[34,89,54,20,50,76,10,45,90] output: 34

def third_smallest(lstofnums):
    unique_sorted = sorted(set(lstofnums))  # Remove duplicates and sort
    return unique_sorted[2] if len(unique_sorted) >= 3 else "Not enough elements"

nums = [34, 89, 54, 20, 50, 76, 10, 45, 90]
print("Third smallest number:", third_smallest(nums))
