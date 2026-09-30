## Q] Print Nth occurrence in the list.

y = [20, 40, 40, 40, 50, 60]
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

# Find Nth Occurrence
def Nth_element(y, key, n):
    if n <= 0:
        return -1
    first = Searching_Data(y, key)
    Position = first + (n - 1)
    if first != -1 and 0 <= Position < len(y) and y[Position] == key:
        return Position
    return -1


print("0th element:-->", Nth_element(y, 40, 0))
print("1st element:-->", Nth_element(y, 40, 1))
print("2nd element:-->", Nth_element(y, 40, 2))
print("3rd element:-->", Nth_element(y, 40, 3))
print("4th element:-->", Nth_element(y, 40, 4))
