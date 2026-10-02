# Problem: Selection Sort
#
# Given an array, sort the elements in ascending order
# using Selection Sort.
#
# Example:
# Input:  [64, 25, 12, 22, 11]
#
# Output:
# [11, 12, 22, 25, 64]

### Tracing Part -
# Start from the first element.
# Here we have to take one assumed position or minimum position.
# Now assume the first element is the smallest, means minimum position = first position
# Compare it with all remaining elements.
# if condition become True change the minimum position with current position
# again start checking until condition become False
# at the end after checking all the elements we have to swap starting first minimum position with current minimum position.

# Note - if condition become True we will not swapping here , we have to change the minimum postion.
# At the end we will change the 2st and current min position


arr = [64, 25, 12, 22, 11]
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

result = selection_sort(arr)    ## stored here output of selection_sort function
print("Sorted Array:", result)

# Time Complexity:
# Best Case: O(n²)
# Average Case: O(n²)
# Worst Case: O(n²)

# Space Complexity: O(1)
