# Problem: Merge Sort
#
# Given an array, sort the elements in ascending order
# using Merge Sort.
#
# Example:
# Input:  [30, 20, 7, 17, 31, 4, 1]
#
# Output:
# [1, 4, 7, 17, 20, 30, 31]

### Tracing Part -
# Divide the array into two halves.
# Continue dividing until each part contains one element.
# Merge the smaller arrays in sorted order.
# Compare elements from both parts.
# Add the smaller element to the result.
# Continue until both parts are completely merged.

# Note - Merge is working on the basis of divide and conquer.  ## conquer == merge

x = [30, 20, 7, 17, 31, 4, 1]
def Divide(x, low, high):
    if low>=high:
        return
    mid = (low+high)//2
    left = x[low:mid+1:]
    right = x[mid+1::]
    print(left, right)
    Divide(x,low,mid)
    Divide(x,mid+1,high)
    Merge(x, low, mid, high)
Divide(x,0,len(x)-1)
print("Final Sorted Array--->",x)

def Merge(x, low, high, mid):
    k=low                   ## low=0
    i=0
    j=0
    while i<len(low) and j<len(right):
        if left[i]<right[j]:
            x[k] = left[i]
            k=k+1
            i=+1
        else:
            x[k] = right[j]
            k=k+1
            j=j+1
    while i<len(low):
        x[k] = left[i]
        k=k+1
        i=i+1
    while j<len(right):
        x[k] = right[j]
        k=k+1
        j=j+1
    print("Merging List---->",x[low:high+1:1])
