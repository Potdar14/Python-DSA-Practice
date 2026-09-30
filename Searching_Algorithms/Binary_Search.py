# Problem: Binary Search
#
# Given a sorted array and a target element,
# find the index of the target element.
#
# Example:
# Input:  [10, 20, 30, 40, 50, 60, 70]
# Target: 60
#
# Output:
# Element found at index 5

### Tracing Part -
# Binary Search works only on a sorted array.
# Set low at the first index.
# Set high at the last index.
# Find the middle index using (low + high) // 2.
# Compare the middle element with the target.
# If they are equal → return the middle index.
# If target is greater than middle element → search the right half.
# If target is smaller than middle element → search the left half.
# Continue until the element is found or low becomes greater than high.
# If low becomes greater than high → element is not present.


arr = [10, 20, 30, 40, 50, 60, 70]
target = 60
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

result = binary_search(arr, target)   ## stored here output of binary_search function
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")

  
# Time Complexity:
# Best Case: O(1)
# Average Case: O(log n)
# Worst Case: O(log n)

# Space Complexity: O(1)
