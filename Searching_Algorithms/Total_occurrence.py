## Q] Find total occurrence of an element in the list.

y = [20, 40, 40, 40, 40, 50, 60]
key = 40

# Find First Occurrence
def Searching_Data(y, key):
    li = 0
    hi = len(y) - 1
    first = -1
    while li <= hi:
        mid = (li + hi) // 2
        if key == y[mid]:
            first = mid
            hi = mid - 1
        elif key > y[mid]:
            li = mid + 1
        else:
            hi = mid - 1
    return first

# Find Last Occurrence
def Searching_Data2(y, key):
    li = 0
    hi = len(y) - 1
    last = -1
    while li <= hi:
        mid = (li + hi) // 2
        if key == y[mid]:
            last = mid
            li = mid + 1
        elif key > y[mid]:
            li = mid + 1
        else:
            hi = mid - 1
    return last

# Find Total Occurrence
def Total_Occurrence(y, key):
    first = Searching_Data(y, key)
    if first == -1:
        return 0
    last = Searching_Data2(y, key)
    total = last - first + 1
    return total

print("Total Occurrence:", Total_Occurrence(y, key))
