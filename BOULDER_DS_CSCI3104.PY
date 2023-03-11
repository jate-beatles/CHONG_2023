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
###############################################################################
#  Heap and Hashtable Data Structure
# 
#-------------------------------------------------------------------------------
# DynamicArray: 

class DynamicArray: 
    
    def __init__(self, initial_size=16, initial_fill=0, debug=False):
        self.allocated_size = initial_size 
        self.size = 0
        self.array = [initial_fill] * initial_size
        self.debug = debug
    
    # This allows us to directly access d[idx]
    def __getitem__(self, idx):
        assert idx >= 0 and idx < self.size 
        return self.array[idx]
    
    # This allows us to write d[idx] = val 
    def __setitem__(self, idx, val):
        assert idx >= 0 and idx < self.size 
        self.array[idx] = val
    
    def append(self, x):
        # Do we have enough allocated size to just append x to the array?
        if self.size >= self.allocated_size:
            if self.debug: 
                print(f'Ran out of memory: old allocated size: {self.allocated_size}, new allocated size is {2*self.allocated_size}')
            # No, we have run out of pre-allocated memory
            # Double the size of the array 
            # Double the size of the allocated memory
            self.allocated_size = 2 * self.allocated_size
            old_array = self.array
            # allocate and copy.
            new_array = allocateMemory(self.allocated_size)
            copyInto(old_array, new_array)
            # update the array.
            self.array = new_array
        # Append the element to the end
        self.array[self.size] = x
        # Update its size.
        self.size = self.size + 1

l = DynamicArray(initial_size=1, initial_fill=0, debug=True)
for j in range(1000):
    l.append(j)
    
print(f'l[5] = {l[5]}')
l[0] = 30
print(f'l[0] = {l[0]}')

# Ran out of memory: old allocated size: 1, new allocated size is 2
# Ran out of memory: old allocated size: 2, new allocated size is 4
# Ran out of memory: old allocated size: 4, new allocated size is 8
# Ran out of memory: old allocated size: 8, new allocated size is 16
# Ran out of memory: old allocated size: 16, new allocated size is 32
# Ran out of memory: old allocated size: 32, new allocated size is 64
# Ran out of memory: old allocated size: 64, new allocated size is 128
# Ran out of memory: old allocated size: 128, new allocated size is 256
# Ran out of memory: old allocated size: 256, new allocated size is 512
# Ran out of memory: old allocated size: 512, new allocated size is 1024
# l[5] = 5
# l[0] = 30

# Mean Heap is the each of the parent is less or equal to it's childrens 
# Heap is binary trees with special laid out of the arry 
# 

# Heap operation  - deleted the element of the heap 
#                 - insert the element into the heap 
#### Bubble up  & Bubble down 
# Imagine the heap is broken - one of child is in wrong postion 
#### Bubble up to swap the child with the child 
#########################################################################################
# Pseudo Code for the Bubble UP 
# bubble up ( A, j) : 
#     if j <= 1: 
#         return
#     else: 
#         if A[j] <= A[j//2]:
#             swap( A[j], A[j//2])
#             bubbleup(A,j//2)
########################################### Bubble up  = theta ( log2(n))


################## Heap sort --- insert/delete / heapify  -----priority of Q

# s1: how to insert --conplexity - theta(log(2)n)
#     1.append the e to the heap array
#     2.bubbleup(a,n+1)
# s2: delete the e of the heap k --complexity theta(log(2)n)
#     delete - then a hole happen -- replace the delete the aj wiht an
#     adjust the size to n-1
#     fix the broken -- bubble up if aj is the less than the parent
#                     -- bubble down if the aj is greater than ist children 
#     complexity of the deletion - 1. swap 2.adjust 3.bubbleup bdown
# s3: find the smallest in the heap -- heapify algorithm - complexity theta (n)
#     application: Q called priority q 
#     FIFO  que  - shedule/parket - the insertion que have different priority 
#     random array which turn into a heap - [mean heap]  
                        
#     sinply idea: for i = n/2 down to 1  then bubbledown(a,i) #a is a mean heap  
#     complexity of heapify: is the lnear of the size array theta(n)
# s4: heap sort, sort the array in ascending array
#     1. heapify(a)  insert:
#     2. delete
#                       
#
###################### Hastables : Basic Introduction 
# hashtable is table  - slots/ bouckets / bin /   each row has the key and the value 
#                         
#       row and column 
# hash() is more efficiently compute for the hash value to find in the hashtable 
# not hte unique key but lots of keys 
# hash() should alone with the table, you can map lots key in same slot table 
# ###hot to insert the hastable 
#lots of keys into same key --- how to handle the collision 
# 
#  handle collision  -  s1. chaining [insert the same key and value into the append of the key]
#                           delete, find the slot, search in the list of the slots 
#                           cost - if all elemets collide onto the 1 slot: in the worst case -- search for the entire slots, and bigO(n) 
#                           load factors --- number of the value insert into hashtable / slots 
#                           
#                       s2. Rehasing the hashtable, each element of old hash change to new hashtable, if empty calculate the hash value 
#                            
#        
#Concluding Thoughts 
# 
# 
#  
#                    - 
# 




