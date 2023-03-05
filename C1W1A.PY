def findCrossoverIndexHelper(x, y, left, right):
    assert(len(x) == len(y))
    assert(left >= 0)
    assert(right < len(x))
    # assert(x[left] > y[left])  # removed

    if left >= right:
        return None

    mid = (left + right) // 2
    if x[mid] >= y[mid]:
        return findCrossoverIndexHelper(x, y, left, mid)
    else:
        result = findCrossoverIndexHelper(x, y, mid+1, right)
        if result is not None:
            return result
        else:
            return mid


def findCrossoverIndex(x, y):
    assert(len(x) == len(y))
    assert(x[0] > y[0])
    n = len(x)
    assert(x[n-1] < y[n-1])

    return findCrossoverIndexHelper(x, y, 0, n-1)
    return findCrossoverIndexHelper(x, y, 0, n-1)



print(findCrossoverIndex([0, 1, 2, 3, 4, 5, 6, 7], [-2, 0, 4, 5, 6, 7, 8, 9]))

