# def findCrossoverIndexHelper(x, y, left, right):
#     # Note: Output index i such that 
#     #         left <= i <= right
#     #         x[i] <= y[i]
#     # First, Write down our invariants as assertions here
#     assert(len(x) == len(y))
#     assert(left >= 0)
#     assert(left <= right-1)
#     assert(right < len(x))
#     # Here is the key property we would like to maintain.
#     assert(x[left] > y[left])
#     assert(x[right] < y[right])

#     if left >= right:
#         return None

#     mid = (left + right) // 2
#     if x[mid] > y[mid] and x[mid+1] < y[mid+1]:
#         return mid
#     elif x[mid] > y[mid]:
#         return findCrossoverIndexHelper(x, y, mid+1, right)
#     else:
#         return findCrossoverIndexHelper(x, y, left, mid -1)


# def findCrossoverIndex(x, y):
#     assert(len(x) == len(y))
#     assert(x[0] > y[0])
#     n = len(x)
#     assert(x[n-1] < y[n-1])

#     return findCrossoverIndexHelper(x, y, 0, n-1)

def findCrossoverIndexHelper(x, y, left, right):
    # Note: Output index i such that 
    #         left <= i <= right
    #         x[i] <= y[i]
    # First, Write down our invariants as assertions here
    assert(len(x) == len(y))
    assert(left >= 0)
    assert(left <= right-1)
    assert(right < len(x))
    # Here is the key property we would like to maintain.
    assert(x[left] > y[left])
    assert(x[right] < y[right])
    
    # your code here
    mid = (left + right) //2 
    if x[mid] > y[mid] and x[mid+1] < y[mid+1]:
        return mid
    elif x[mid] > y[mid]: 
        return findCrossoverIndexHelper(x, y, mid+1, right)
    else:
        return findCrossoverIndexHelper(x, y, left, mid-1) 
    
def findCrossoverIndex(x, y):
    assert(len(x) == len(y))
    assert(x[0] > y[0])
    n = len(x)
    assert(x[n-1] < y[n-1]) # Note: this automatically ensures n >= 2 why?

    return findCrossoverIndexHelper(x,y,0,n-1)

print(findCrossoverIndex([0, 1, 2, 3, 4, 5, 6, 7], [-2, 0, 4, 5, 6, 7, 8, 9]))
print(findCrossoverIndex([0, 2, 4, 5, 6, 7, 8,10], [-2, 0, 2, 4, 7, 8, 10, 12]))
print(findCrossoverIndex([0, 1], [-10, 10]))
print(findCrossoverIndex([0, 1, 2, 3, 4, 5, 6, 7], [-2, 0, 4, 4.2, 4.3, 4.5, 8, 9]))
print(findCrossoverIndex([0,1, 2, 3], [-10, -9, -8, 5]))

