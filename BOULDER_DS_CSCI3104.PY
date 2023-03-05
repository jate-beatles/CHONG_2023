#This is my vour for my 2025 tour, ONLY 2 YEARS LEFT 
###
#Algorithm for is 
# input - ALG - ouput
#
#Behind the computing: Computational Procedures 
#Buy a book name >>>>> The art of computer Programming #
#Algorithms in the searching
## https://www.manning.com/books/grokking-algorithms
####CLRS
 # THere is only to 

# 1.the output must be sort according to the provided order
# 2.output must be sorted according to <= 
# 3.Bubble Sort/ Magic Sort / Heap Sort / Quick Sort  } - Tim sort   most use = quicksort 
####pseudo-code conventions
####Insertion sort procedure
####insert( A, j) 
        # for i = j - 1 down to (i) 
        #   if A[i] >   A[i+1] : 
        #     swap ( A[i], A[i+1])
        #   else : 
        #      break;

        # for j = 1 up to n : 
        #     insert(A,j) 

# Computation Complaxity 
#    Time: Independent 
#    Space:Memory 


#The best case of the insertion: Break when the first insertion happen 
#

def fun(n,x):
    counter = n
    amount = 0
    while counter > 0:
        amount = amount + x
        counter = counter - 1
    return amount

#### Cost model for each operation cost 

####Asymptotic Notation 
# In mathematics (logic), the symbol ∃

    # ∃ is read as "there exists" and the symbol 
    # ∀
    # ∀ is read as for all. 

# f(g) = BIG O g(). ignore any addtional and coefficient that put on the function, compare the power firstly
# Big O for comparing the function of the overtaken 

####  f = O(g)  which is the asymptotic upper bound 
#      e.g.: 200000* n^2 = [<=] O (0.00000000002* n^3) 
#              
###   f = OMEGA (g) which is the asymptotic lower bound 
#      e.g.: 

####  Big Theta Quatation  f = Big Theta (g)      : which is the asymptotic equal


#### Asymtotics Examples 
# COMPANY THE LOG AND N SQUARE, WHICH THE N SQUARE IS MORE PROMINENT 

####Analysis of Algorithms  - Binary Search
#      key idea:    S1. find the mid = ( left + right) // 2
#                   S2. find the new mid again 
#                   S3. find the index mide number, if not /= target
#                   S4. return w


#### Binary SEARCH IMPLEMENTATION
#    the time analysis is the that in the worst scanirao  k = log2(n)
#               thus 


### Analysis fo the Alogrithms  - Merge Sort 
#        split the order, then sort, then merge 

# pseudocode
# 
#   
# Merger procedure Correctness Argument 
# Merger running time is the BIG THETA of the [right - left + 1]
# 

def mergesort ( array, left, right)
    if ( left >= right):
        return
    if (left + 1 == right):
    if lst[left] > lst[right]:
     swap(lst, left, right)
     return
    else
    mid = (left + right)//2
    mergesort(array, left, mid)
    mergesort(array, mid+1, right)
    
    merge(array, left, mid, right)

def merge(array, left, mid, right):
i = left
j = mid + 1
tmp_store = []

while (i <= mid and j <= right):
     if (array[i] < array[j]):
        #append array[i] to tmp_store
        i = i + 1
     else:
        #append array[j] to tmp_store
        j = j + 1

if i < mid:
       #Copy remainder of first part to tmp_store
if j < right:
 #Copy remainder of second part to tmp_store
 #copy back from tmp_store into array[left..right]


###############################################################################




