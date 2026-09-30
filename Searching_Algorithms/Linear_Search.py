# Problem: Linear Search
#
# Given an array and a target element,
# find the index of the target element.
#
# Example:
# Input:  [10, 25, 30, 45, 50]
# Target: 45
#
# Output:
# Element found at index 3

### Tracing Part - 
# Start from the first element.
# Compare each element with the target.
# If they are equal → return the index.
# Otherwise, move to the next element.
# Continue until the element is found or the array ends.
# If the array ends → element is not present.


arr = [10, 25, 30, 45, 50]
target = 45
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
result = linear_search(arr, target)   ## stored here output of linear_search function
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")


# Time Complexity:
# Best Case: O(1)
# Average Case: O(n)
# Worst Case: O(n)
  
# Space Complexity: O(1)
