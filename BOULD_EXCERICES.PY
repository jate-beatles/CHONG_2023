# import math

# A = [4,7,12]
# def algorithm compute_array_stuff ( a )
# a is an array of size n 


# for k = 1 to n : 
#     if a[k] is prime: 
#         return 0
# sum = 0      

# for i = 1 to n: 
#     for j = i + 1 to n: 
#         sum = sum + a[i] * a[j]
#     return sum 

def compute_array_stuff(a):
    # a is an array of size n
    n = len(a)
    for k in range(n):
        if is_prime(a[k]):
            return 0
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum = sum + a[i] * a[j]
    return sum

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

A = [4,9,12]
result = compute_array_stuff(A)

def compute_array_stuff_in1line(a):
    if any(is_prime(x) for x in a):
        return 0
    return sum(a[i]*a[j] for i in range(len(a)) for j in range(i+1, len(a)))


result2 = compute_array_stuff_in1line(A)
print(result2)




def findCrossoverIndex(x, y):
    assert(len(x) == len(y))
    assert(x[0] > y[0])
    n = len(x)
    assert(x[n-1] < y[n-1])

    def findCrossoverIndexHelper(x, y, left, right):
        assert(len(x) == len(y))
        assert(left >= 0)
        assert(left <= right-1)
        assert(right < len(x))
        assert(x[left] > y[left])

        if left == right:
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

    return findCrossoverIndexHelper(x, y, 0, n-1)

print (findCrossoverIndex([0, 1, 2, 3, 4, 5, 6, 7], [-2, 0, 4, 5, 6, 7, 8, 9]))


