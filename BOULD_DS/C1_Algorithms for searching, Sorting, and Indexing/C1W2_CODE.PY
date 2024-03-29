#### Basic Datastructures and Heaps 
######################################################
####################MinHeap

class MinHeap:
    def __init__(self):
        self.H = [None]
        # It initializes the heap with an empty list H with a None element at index 0.
 
    def size(self):
        return len(self.H)-1
    
    def __repr__(self):
        return str(self.H[1:])
        
    def satisfies_assertions(self):
        for i in range(2, len(self.H)):
            assert self.H[i] >= self.H[i//2],  f'Min heap property fails at position {i//2}, parent elt: {self.H[i//2]}, child elt: {self.H[i]}'
    
    def min_element(self):
        return self.H[1]

    ## bubble_up function at index
    ## WARNING: this function has been cut and paste for the next problem as well 
    def bubble_up(self, index):
        assert index >= 1
        if index == 1: 
            return 
        parent_index = index // 2
        if self.H[parent_index] < self.H[index]:
            return 
        else:
            self.H[parent_index], self.H[index] = self.H[index], self.H[parent_index]
            self.bubble_up(parent_index)
    
    ## bubble_down function at index
    ## WARNING: this function has been cut and paste for the next problem as well 
    def bubble_down(self, index):
        assert index >= 1 and index < len(self.H)
        lchild_index = 2 * index
        rchild_index = 2 * index + 1
        # set up the value of left child to the element at that index if valid, or else make it +Infinity
        lchild_value = self.H[lchild_index] if lchild_index < len(self.H) else float('inf')
        # set up the value of right child to the element at that index if valid, or else make it +Infinity
        rchild_value = self.H[rchild_index] if rchild_index < len(self.H) else float('inf')
        # If the value at the index is lessthan or equal to the minimum of two children, then nothing else to do
        if self.H[index] <= min(lchild_value, rchild_value):
            return 
        # Otherwise, find the index and value of the smaller of the two children.
        # A useful python trick is to compare 
        min_child_value, min_child_index = min ((lchild_value, lchild_index), (rchild_value, rchild_index))
        # Swap the current index with the least of its two children
        self.H[index], self.H[min_child_index] = self.H[min_child_index], self.H[index]
        # Bubble down on the minimum child index
        self.bubble_down(min_child_index)
        
    def insert(self, elt): 
        self.H.append(elt)
        self.bubble_up(len(self.H)-1)

    def delete_min(self):
        if len(self.H) == 1:
            return None
        min_elt = self.H[1]
        last_elt = self.H.pop()

        if len(self.H) > 1: 
            self.H[1] = last_elt
            self.bubble_down(1) 
        return min_elt
    

###############################################################################    
###################################Top k heap - 
###############################################################################
#Modify the minheaps which hold two arrays : a sorted array A of k 
#                                            MinHeap H remain the n-k ele
# The top K heap design two arryas : H must be  minheap size(n-k)
#                                    A muste sorted of size k 
#                                    every ele of the A must be smaller than ele of H 
#                                

class TopKHeap:
    
    # The constructor of the class to initialize an empty data structure
    def __init__(self, k):
        self.k = k
        self.A = []
        self.H = MinHeap()
        
    def size(self): 
        return len(self.A) + (self.H.size())
    
    def get_jth_element(self, j):
        assert 0 <= j < self.k-1
        assert j < self.size()
        return self.A[j]
    
    def satisfies_assertions(self):
        # is self.A sorted
        for i in range(len(self.A) -1 ):
            assert self.A[i] <= self.A[i+1], f'Array A fails to be sorted at position {i}, {self.A[i], self.A[i+1]}'
        # is self.H a heap (check min-heap property)
        self.H.satisfies_assertions()
        # is every element of self.A less than or equal to each element of self.H
        for i in range(len(self.A)):
            assert self.A[i] <= self.H.min_element(), f'Array element A[{i}] = {self.A[i]} is larger than min heap element {self.H.min_element()}'
        
    # Function : insert_into_A
    # This is a helper function that inserts an element `elt` into `self.A`.
    # whenever size is < k,
    #       append elt to the end of the array A
    # Move the element that you just added at the very end of 
    # array A out into its proper place so that the array A is sorted.
    # return the "displaced last element" jHat (None if no element was displaced)
    def insert_into_A(self, elt):
        k = self.k
        print("k = ", k)
#         assert(self.size() < k)
        self.A.append(elt)
        j = len(self.A)-1
        while (j >= 1 and self.A[j] < self.A[j-1]):
            # Swap A[j] and A[j-1]
            (self.A[j], self.A[j-1]) = (self.A[j-1], self.A[j])
            j = j -1 
        return
    # bug here. it should be self.k (or add k = self.k)
    # bug assert(self.size() < k) ????
    
            
    # Function: insert -- insert an element into the data structure.
    # Code to handle when self.size < self.k is already provided
    def insert(self, elt):
        size = self.size()
        # If we have fewer than k elements, handle that in a special manner
        if size <= self.k:
            self.insert_into_A(elt)
            return 
        # Code up your algorithm here.
        # your code here
        # strategy: 
        # 1. call insert_into_A, len(k) become k+1 temperally
        # 2. pop A[-1] and insert A[-1] to H (call H.insert(elt)), then len(A) back to k
        self.insert_into_A(elt)
        self.H.insert(self.A.pop(-1))
        
    # Function: Delete top k -- delete an element from the array A
    # In particular delete the j^{th} element where j = 0 means the least element.
    # j must be in range 0 to self.k-1
    def delete_top_k(self, j):
        k = self.k
        assert self.size() > k # we need not handle the case when size is less than or equal to k
        assert j >= 0
        assert j < self.k
        # your code here
        # strategy:
        # 1. delete: (when j < k, checked) call A.pop(j)
        # 2. refill: A.append(H[1]), no need to update for A (since we can assure any a in A is larger than any h in H)
        # 3. update H: call H.delete_min
        self.A.pop(j)
        self.A.append(self.H.min_element())
        self.H.delete_min()
        
h = TopKHeap(5)
# Force the array A
h.A = [-10, -9, -8, -4, 0]
# Force the heap to this heap
[h.H.insert(elt) for elt in  [1, 4, 5, 6, 15, 22, 31, 7]]

print('Initial data structure: ')
print('\t A = ', h.A)
print('\t H = ', h.H)


####################################################################################################
####################################################################################################
# Problem 2: Heap data structure to mantain/extract median (instead of minimum/maximum key)
# We have seen how min-heaps can efficiently extract the smallest element efficiently and maintain the least element as we insert/delete elements. Similarly, max-heaps can maintain the largest element. In this exercise, we combine both to maintain the "median" element.

# The median is the middle element of a list of numbers.

# If the list has size  𝑛
#   where  𝑛
#   is odd, the median is the  (𝑛−1)/2𝑡ℎ
#   element where  0𝑡ℎ
#   is least and  (𝑛−1)𝑡ℎ
#   is the maximum.
# If  𝑛
#   is even, then we designate the median the average of the  (𝑛/2−1)𝑡ℎ
#   and  (𝑛/2)𝑡ℎ
#   elements.
# Example
# List is  [−1,5,4,2,3]
#   has size  5
#  , the median is the  2𝑛𝑑
#   element (remember again least element is designated as  0𝑡ℎ
#  ) which is  3
#  .
# List is  [−1,3,2,1]
#   has size  4
#  . The median element is the average of  1𝑠𝑡
#   element (1) and  2𝑛𝑑
#   element (2) which is  1.5
#  .
# Maintaining median using two heaps.
# The data will be maintained as the union of the elements in two heaps  𝐻min
#   and  𝐻max
#  , wherein  𝐻min
#   is a min-heap and  𝐻max
#   is a max-heap. We will maintain the following invariant:

# The max element of  𝐻max
#   will be less than or equal to the min element of  𝐻min
#  .
# The sizes of  𝐻𝑚𝑎𝑥
#   and  𝐻𝑚𝑖𝑛
#   are equal (if number of elements in the data structure is even) or  𝐻𝑚𝑎𝑥
#   may have one less element than  𝐻𝑚𝑖𝑛
#   (if the number of elements in the data structure is odd).
# (A) Design algorithm for insertion.
# Suppose, we have the current data split between  𝐻𝑚𝑎𝑥
#   and  𝐻𝑚𝑖𝑛
#   and we wish to insert an element  𝑒
#   into the data structure, describe the algorithm you will use to insert. Your algorithm must decide which of the two heaps will  𝑒
#   be inserted into and how to maintain the size balance condition.

# Describe the algorithm below and the overall complexity of an insert operation. This part will not be graded.


###############################################################################################################
class MaxHeap:
    def __init__(self):
        self.H = [None]
        
    def size(self):
        return len(self.H)-1
    
    def __repr__(self):
        return str(self.H[1:])
        
    def satisfies_assertions(self):
        for i in range(2, len(self.H)):
            assert self.H[i] <= self.H[i//2],  f'Maxheap property fails at position {i//2}, parent elt: {self.H[i//2]}, child elt: {self.H[i]}'
    
    def max_element(self):
        return self.H[1]
    
    def bubble_up(self, index):
        # your code here
        parent_index = index//2
        if parent_index >= 1 and self.H[parent_index] < self.H[index]:
            self.H[parent_index], self.H[index] = self.H[index], self.H[parent_index]
            self.bubble_up(parent_index)        
            
    
    def bubble_down(self, index):
        # your code here
        left_child_index = 2 * index
        right_child_index = 2 * index + 1
        largest = index
        if left_child_index <= self.size() and self.H[left_child_index] > self.H[largest]:
            largest = left_child_index
        if right_child_index <= self.size() and self.H[right_child_index] > self.H[largest]:
            largest = right_child_index
        if largest != index:
            self.H[largest], self.H[index] = self.H[index], self.H[largest]
            self.bubble_down(largest)       
        
        
    
    # Function: insert
    # Insert elt into minheap
    # Use bubble_up/bubble_down function
    def insert(self, elt):
        # your code here
        # strategy: 1. insert at the end, (note: the index start at position 1)
        # 2.only need to check parents (call bubble_up)
        self.H.append(elt)
        index = self.size()
        self.bubble_up(index)
        self.satisfies_assertions()        
        
    # Function: delete_max
    # delete the largest element in the heap. Use bubble_up/bubble_down
    def delete_max(self):
        # your code here
        # stratgegy: delete the min (index==1), replace with the last element, then rebuild heap 
        # 1. use the last element to inplace the delete element (pop()). 
        # 2. then call bubble_down
        # (note: the index start at position 1)
        if self.size() == 0:
            return None
        max_elt = self.H[1]
        self.H[1] = self.H[-1]
        del self.H[-1]
        self.bubble_down(1)
        self.satisfies_assertions()
        return max_elt 
    
####################################################################################################
class MedianMaintainingHeap:
    def __init__(self):
        self.hmin = MinHeap()
        self.hmax = MaxHeap()
        
    def satisfies_assertions(self):
        if self.hmin.size() == 0:
            assert self.hmax.size() == 0
            return 
        if self.hmax.size() == 0:
            assert self.hmin.size() == 1
            return 
        # 1. min heap min element >= max heap max element
        assert self.hmax.max_element() <= self.hmin.min_element(), f'Failed: Max element of max heap = {self.hmax.max_element()} > min element of min heap {self.hmin.min_element()}'
        # 2. size of max heap must be equal or one lessthan min heap.
        s_min = self.hmin.size()
        s_max = self.hmax.size()
        assert (s_min == s_max or s_max  == s_min -1 ), f'Heap sizes are unbalanced. Min heap size = {s_min} and Maxheap size = {s_max}'
    
    def __repr__(self):
        return 'Maxheap:' + str(self.hmax) + ' Minheap:'+str(self.hmin)
    
    def get_median(self):
        if self.hmin.size() == 0:
            assert self.hmax.size() == 0, 'Sizes are not balanced'
            assert False, 'Cannot ask for median from empty heaps'
        if self.hmax.size() == 0:
            assert self.hmin.size() == 1, 'Sizes are not balanced'
            return self.hmin.min_element()
        # your code here
        if self.hmin.size() == 0:
            assert self.hmax.size() == 0, 'Sizes are not balanced'
            assert False, 'Cannot ask for median from empty heaps'
        if self.hmax.size() == 0:
            assert self.hmin.size() == 1, 'Sizes are not balanced'
            return self.hmin.min_element()
        if self.hmin.size() == self.hmax.size():
            return (self.hmin.min_element() + self.hmax.max_element()) / 2
        else:
            return self.hmin.min_element()       
    
    # function: balance_heap_sizes
    # ensure that the size of hmax == size of hmin or size of hmax +1 == size of hmin
    # If the condition above does not hold, move the max element from max heap into the min heap or
    # vice versa as needed to balance the sizes.
    # This function could be called from insert/delete_median methods
    def balance_heap_sizes(self):
        # your code here
        if self.hmax.size() > self.hmin.size() + 1:
            elt = self.hmax.max_element()
            self.hmax.delete_max()
            self.hmin.insert(elt)
        elif self.hmin.size() > self.hmax.size() + 1:
            elt = self.hmin.min_element()
            self.hmin.delete_min()
            self.hmax.insert(elt)     
    
    def insert(self, elt):
        # Handle the case when either heap is empty
        if self.hmin.size() == 0:
            # min heap is empty -- directly insert into min heap
            self.hmin.insert(elt)
            return 
        if self.hmax.size() == 0:
            # max heap is empty -- this better happen only if min heap has size 1.
            assert self.hmin.size() == 1
            if elt > self.hmin.min_element():
                # Element needs to go into the min heap
                current_min = self.hmin.min_element()
                self.hmin.delete_min()
                self.hmin.insert(elt)
                self.hmax.insert(current_min)
                # done!
            else:
                # Element goes into the max heap -- just insert it there.
                self.hmax.insert(elt)
            return 
        # Now assume both heaps are non-empty
        # your code here
        #         if elt >= self.hmax.max_element():
#             self.hmin.insert(elt)
#         else:
#             self.hmax.insert(elt)
        # note: (based on the implementation invariables, aka assert), we need to insert element into hmin
        # self.hmin.insert(elt)
        # self.balance_heap_sizes() 
        
        if elt < self.hmax.max_element():
            self.hmax.insert(elt)
        else:
            self.hmin.insert(elt)
        self.balance_heap_sizes()      
        
    def delete_median(self):
        self.hmax.delete_max()
        self.balance_heap_sizes()