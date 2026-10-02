# Problem: Insertion Sort
#
# Given an array, sort the elements in ascending order
# using Insertion Sort.
#
# Example:
# Input:  [12, 11, 13, 5, 6, 1, 45]
#
# Output:
# [1, 5, 6, 11, 12, 13, 45]


### Tracing Part -
# Here we have to check with previous element
# Start from the 1st position bcoz at 0th position there will be no previous value to compare.
# Store the current element as key.
# Compare key with the elements before it.
# Always we have to check until 0th position.
# Shift larger elements one position to the right.
# Insert key at its correct position.
# Repeat until the array is sorted.


arr = [12, 11, 13, 5, 6, 1, 45]
def insertion_sort(arr):
  for Pass_data in range(1, len(arr)):
      i = Pass_data
      while i!=0 and arr[i] < arr[i-1]:
          arr[i], arr[i-1] = arr[i-1], arr[i]
          i=i-1
  return arr

result = insertion_sort(arr)       ## stored here output of insertion_sort function
print("Sorted Array:", result)


# Time Complexity:
# Best Case: O(n)
# Average Case: O(n²)
# Worst Case: O(n²)

# Space Complexity: O(1)
