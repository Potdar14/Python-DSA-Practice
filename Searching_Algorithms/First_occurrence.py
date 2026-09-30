## Q] Print 1st occurrence in the list.

r = [2, 5, 8, 10, 99, 105, 105, 105, 200]
key = 105

def Searching_Data(r, key):
    li = 0
    hi = len(x) - 1
    first = -1

    while li <= hi:
        mid = (li + hi) // 2
        if key == x[mid]:
            first = mid
            hi = mid - 1
        elif key > x[mid]:
            li = mid + 1
        else:
            hi = mid - 1
    return first
print("First Occurrence:", Searching_Data(r, key))
