# Problem: Quick Sort

'''
- It will be working on the basis of divide and conquer , but here we have to take one pivot element.
- pivot element - Reference element (we have to take any position element)
- once we assign any pivot element, for sorting collection pivot element should be present in middle and left side 
all the lower elements and in the right side greater values should be present after this our collection 
will sort and we will print it.
- Steps :
  1] consider a list collection.
  2] Initialise three variables i.e pivot as values present at 0th position ,i as 1th and j as len(collection)-1.
  3] check whether i<=j or not,if condition is true then check for following condition.
  4] if collection[i] < pivot if true then increment the value of i by 1 and then again same step(4th one itself).
  5] if 4th step become false then we have to check--> collection[j] > pivot if true then decrement the value of j by 1.
  6] if 4th step and 5th step both conditions become false we have to check 7th step.
  7] if i<=j then swap collection[i] with collection[j].
  8] if i<=j false then swap pivot element with jth element and return the value of j.
  9] after moving pivot element in the middle we have to separate left side and right side , 
       after this we have to sort that both part only and for this we have to take different pivot element.
- left side -> only lower values.
- right side -> only greater values.
'''

# Given an array, sort the elements in ascending order
# using Quick Sort.
#
# Example:
# Input:  [10, 56, 23, 90, 111, 45, 1, 0.5, 1000, 43]
#
# Output:
# [0.5, 1, 10, 23, 43, 45, 56, 90, 111, 1000]

s = [10, 56, 23, 90, 111, 45, 1, 0.5, 1000, 43]
def Sorted(s, low, high):
    P = s[low]              # First element as pivot
    i = low + 1
    j = high
    while i <= j:
        while i <= j and s[i] < P:
            i = i + 1
        while i <= j and s[j] > P:
            j = j - 1
        if i <= j:
            s[i], s[j] = s[j], s[i]
            i = i + 1
            j = j - 1
    s[low], s[j] = s[j], s[low]
    return j
def Quick_Sort(s, low, high):
    if low >= high:
        return
    j = Sorted(s, low, high)
    Quick_Sort(s, low, j - 1)
    Quick_Sort(s, j + 1, high)
Quick_Sort(s, 0, len(s) - 1)
print(s)


# Time Complexity:
# Best Case: O(n log n)
# Average Case: O(n log n)
# Worst Case: O(n²)

# Space Complexity:
# O(log n)
