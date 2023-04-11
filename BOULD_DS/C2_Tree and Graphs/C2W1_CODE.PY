class Node:
    def __init__(self, key, parent = None):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None

        if parent != None: 
            if key < parent.key:
                assert(parent.left == None) 
                parent.left = self
            else:
                assert key > parent.key,'key is same as parent.key. We do not allow duplicate keys in BST SINCE IT BREAKS SOME OF the algorithms'
                assert(parent.right == None),'parent already has a right child -=- unable to create node'
                parent.right = self

    def get_leftmost_descendat(self):
        if self.left !=None:
            return self.left.get_leftmost_descendant()
        else: 
            return self 
                  
    def search(self,key):
        if self.key == key:
            return(True, self)
        else:
            if key > self.key and self.right != None:
                return self.right.search(key)
            if key < self.key and self.left != None:
                return self.left.search(key)
            else: 
                return(False, self)

    def insert(self, key):
        if self.key == key:
            return self
        elif self.key < key:
            if self.right is None:
                self.right = Node(key, self)
                return self.right 
            return self.right.insert(key)
        else: 
            if self.left is None:
                self.left = Node(key,self)
                return self.left
            return self.left.insert(key)


    def height(self):
        if self.left and self.right:
            return 1 + max(self.left.height(), self.right.height())
        elif self.left:
            return 1 + self.left.height()
        elif self.right:
            return 1 + self.right.height()
        else:
            return 1
        
    #: Write an algorithm to delete a key in the tree.
    # First, find the node in the tree with the key.
    # Recommend drawing pictures to visualize these cases below before
    # programming.
    # Case 1: both children of the node are None
    #   -- in this case, deletion is easy: simply find out if the node with key is its
    #      parent's left/right child and set the corr. child to None in the parent node.
    # Case 2: one of the child is None and the other is not.
    #   -- replace the node with its only child. In other words,
    #      modify the parent of the child to be the to be deleted node's parent.
    #      also change the parent's left/right child appropriately.
    # Case 3: both children of the parent are not None.
    #    -- first find its successor (go one step right and all the way to the left).
    #    -- function get_leftmost_descendant may be helpful here.
    #    -- replace the key of the node by its successor.
    #    -- delete the successor node.
    # return: no return value specified        
      
      
    def delete(self, key):
        (found, node_to_delete) = self.search(key)
        assert(found==True), f"key to be delted:{key} - does not exist in the tree"
        parent_node = node_to_delete.parent

        if node_to_delete.left == None and node_to_delete.right == None:
            if node_to_delete == parent_node.left:
                parent_node.left = None
            else:
                parent_node.right = None
    
        if node_to_delete.left ==None or node_to_delete.right == None:
            if node_to_delete.left == None:
                replace_child = node_to_delete.right
            else: 
                replace_child = node_to_delete.left
            if node_to_delete == parent_node.right:
                parent_node.right = replace_child
            else:
                parent_node.left = replace_child

        if node_to_delete != None and node_to_delete!= None:
            successor = node_to_delete.right.get_leftmost_descendat()
            node_to_delete.key = successor.key
            successor.delete(successor.key)


t1 = Node(25, None)
t2 = Node(12, t1)
t3 = Node(18, t2)
t4 = Node(40, t1)

print('-- Testing basic node construction (originally provided code) -- ')
assert(t1.left == t2), 'test 1 failed'
assert(t2.parent == t1),  'test 2 failed'
assert(t2.right == t3), 'test 3 failed'
assert (t3.parent == t2), 'test 4 failed'
assert(t1.right == t4), 'test 5 failed'
assert(t4.left == None), 'test 6 failed'
assert(t4.right == None), 'test 7 failed'           
        
print('-- Testing search -- ')
(b, found_node) = t1.search(18)
assert b and found_node.key == 18, 'test 8 failed'
(b, found_node) = t1.search(25)
assert b and found_node.key == 25, 'test 9 failed -- you should find the node with key 25 which is the root'
(b, found_node) = t1.search(26)
assert(not b), 'test 10 failed'
assert(found_node.key == 40), 'test 11 failed -- you should be returning the leaf node which would be the parent to the node you failed to find if it were to be inserted in the tree.'


import random

# Using the implementation of the binary search tree in part 1, complete the function calculateAverageDepth(n, numTrials) that performs the following experiment numTrials number of times.

# Each experiment run is as follows:
# Take a list of numbers from 0 to n-1.
# Randomly shuffle the list: use random.shuffle function or (advanced) write your own shuffle.
# Insert the randomly shuffled list into a tree.
# Find and return the depth of the tree.


# 1. make list of  numbers from 0 to n-1
# 2. randomly shuffle the list
# 3. insert the random list elements in order into a tree.
# 4. return the height of the resulting ree.
def run_single_experiment(n):
    # your code here
    arr = list(range(n))
    random.shuffle(arr)
    t1 = Node(arr[0], None)
    for elt in arr:
        t1.insert(elt)
    return t1.height()    
    
def run_multiple_trials(n, numTrials):
    lst_of_depths = [run_single_experiment(n) for j in range(numTrials)]
    return (sum(lst_of_depths)/len(lst_of_depths), lst_of_depths)

    
from matplotlib import pyplot as plt
import math

(avg64, lst_of_results_64) = run_multiple_trials(64,1000)
plt.hist(lst_of_results_64)
plt.xlim(0,64)
plt.xlabel('Depth of Tree')
plt.ylabel('Frequency')
plt.title('Histogram of depths for n = 64')
print(f'Average depth for 64 = {avg64}')
assert avg64 <= 12 and avg64 >= 8

plt.figure()
(avg128, lst_of_results_128) = run_multiple_trials(128,1000)
print(f'Average depth for 128 = {avg128}')
assert avg128 <= 16 and avg128 >= 12


plt.hist(lst_of_results_128)
plt.xlim(0,128)
plt.xlabel('Depth of Tree')
plt.ylabel('Frequency')
plt.title('Histogram of depths for n = 128')

nmin=16
nmax=64

lst_of_average_depths = [ run_multiple_trials(j,1000)[0] for j in range(nmin,nmax)]
plt.figure()
l1 = plt.plot(range(nmin,nmax), lst_of_average_depths,label='Avg. Depth')
plt.xlabel('n')
plt.ylabel('depth')
l2 = plt.plot(range(nmin,nmax), [1.6* math.log(j)/math.log(2) for j in range(nmin,nmax)],'--r',label='1.6log2(n)')
l3 = plt.plot(range(nmin,nmax), [2.2* math.log(j)/math.log(2) for j in range(nmin,nmax)],'--b',label='2.2log2(n)')
#plt.legend(handles=[l1, l2, l3])
plt.title('Average depth as a function of n and comparison with 1.6 log2(n), 2.2 log2(n)')
print('Passed all tests -- 15 points')


# Testing deletion
t1 = Node(16, None)
# insert the nodes in the list
lst = [18,25,10, 14, 8, 22, 17, 12]
for elt in lst:
    t1.insert(elt)

# The tree should look like this
#               16
#            /     \
#          10      18
#        /  \     /  \
#       8   14   17  25
#          /         /  
#         12        22


# Let us test the three deletion cases.
# case 1 let's delete node 8
# node 8 does not have left or right children.
t1.delete(8) # should have both children nil.
(b8,n8) = t1.search(8)
assert not b8, 'Test A: deletion fails to delete node.'
(b,n) = t1.search(10)
assert( b) , 'Test B failed: search does not work'
assert n.left == None, 'Test C failed: Node 8 was not properly deleted.'

# Let us test deleting the node 14 whose right child is none.
# n is still pointing to the node 10 after deleting 8.
# let us ensure that it's right child is 14
assert n.right != None, 'Test D failed: node 10 should have right child 14'
assert n.right.key == 14, 'Test E failed: node 10 should have right child 14'

# Let's delete node 14
t1.delete(14)
(b14, n14) = t1.search(14)
assert not b14, 'Test F: Deletion of node 14 failed -- it still exists in the tree.'
(b,n) = t1.search(10)
assert n.right != None , 'Test G failed: deletion of node 14 not handled correctly'
assert n.right.key == 12, f'Test H failed: deletion of node 14 not handled correctly: {n.right.key}'

# Let's delete node 18 in the tree. 
# It should be replaced by 22.

t1.delete(18)
(b18, n18) = t1.search(18)
assert not b18, 'Test I: Deletion of node 18 failed'
assert t1.right.key == 22 , ' Test J: Replacement of node with successor failed.'
assert t1.right.right.left == None, ' Test K: replacement of node with successor failed -- you did not delete the successor leaf properly?'
