# Algorithms that use randomness 
def geometric(p):
    count = 0 
    if flip(p):
        return 1 + geometirc(p)
    else: return 1 
# the worst case is the always flipping the coin 
# why randomness: 
# Aveage Case Complexity: expected case 
# 
##Why randomness in Data-structure - Hashtables / Treaps 
#in many case store not random data, introduce the randomness into data constructure.
#
## Analysis of Algorithms: Recurrences 
#           
####    Partition and Quicksort 
##      Quick Sort - practical methods 
#           Developed by Sin Tony House      
#           Data moement 
#           Divide & Conquer Algorithm 
#           Partition - divide part, chose a pivot - any position, then anythin smaller than then pivo is on the left, bigger ones then on the right
#           -lerf part is less than the pivot, the order is not arranged 
#           3. not arrange the order after partition 
#           4.sort the left part and sort the right part, pivot in the final place 
#           5. quick sort, choose the last item from the order, and partition, and sort
#                    
###     Detailed Patitioning - Quick Sort pyseudo code 
#           Pyseudo code:
#           [a1, .......a[n]]
#              find the pivot, rearrange, a^
#           Lomuto Partition - italiy science - Partition scheme - another in the ipynb
#           THE ARRAY REARRANGEMENT IS IN PLACE, in the intermediate steps: 
#           1. A: [ ..........x] - divide into 3 regions
#              the whole region is unprocess at the beginning  
#           2. everything in region1 is less than the pivo, region2 greater than pivot,
#              then, last region is the unprocess region
#              the region1 less then the pivot 
#           3. swap the ele in the region1 a[i+1] swap with the a[j] if a[j] < x<  
#              then the entire: 
#           while (j < n-1) : #unprocess is empty
#               if A[j] < x: 
#               initially region1 and region2 is empty, i = 0, j = 1 
#               everything is unprocess in the region3
#               swap(A, i+1, j) 
#               i += 1 
#               j += 1
#           else:
#               j += 1 
#           swap (A, i+1, n)
#           return i+1
###     Practice Sample Partition Schemes 
#
#            i, j index 0 1
#                     [ 3,1, 7, 8, 4, 2, 10, 9, 5]
#               if A[1] < 5:
#               swap(A,i+1, j) # swap(A, 1,1,)
#               i +=1
#               j +=1   
#            i, j index 0 1 2     [j = 2]
#                        [3,1,l, 8, 4, 2, 10, 9, 5]
#                   
##          the running time is just n of the array for the partition, pyseudo code, from the i = 0, j = 1;
#                                  
#                      
###     Quick Sort i- in the worst case analysis
#               the pivot can be the largest element in the array
#               the complexity goes to theta(n^2) - every poorly in the worst case 
#           strategy of quick sort is to find the good pivot 
#           choose the median of the array, how to find the good pivot, determinist of the chossing the pivot, or pseudo random number as the pivot 
###     The expected complexity - of quicksort is = nlogn
##          the prability = 1/n, the prabability of chosen eht smallest is 1/n
#           T(n) = exepcted avg on the ele =      
#                = 1/n [SumT(i) + T(n-i)]  = 2/n(sumT(i)) + Cn
#                = ...
#                = theta(nlog(n))
#
#
####    Quick Select 
#           find the kth smallest ele in the A 
#           what the naive algorithm to select = theta(nlogn)
#           
#           1. for i = i to k, find the samllest ele in A, complexity = theta (nk)
#           
###     Using the quick select to pick up the kth smallest element 
#           pivot the array, and partition, the pivot is the j[th] element
#           1. case 1:  j = k 
#               return x 
#           2. case 2: j > k, the recusively the quickselect of the region ( A[1] -- A[j-1])
#               looking for the left region
#           3. case 3: j < k, then quickselect [A(j+1) .....   (k-j)]  smallest 
##      W.C worst case of thel complexity 
#           the complexity  = Thera (n^2) 
#      
####    Analysis of the randomness Quickselect 
##                
# 
#      
#############################################################
####        Hash Function 
#               what is the great hash function
#               fewer collision 
##          Hash is no the data structure 
##          How to design hash functions 
#            - randomized the elements 
#            - hash function do not suffer form the collision 
##          Example 1: 
#               hash([a1, a2, ...an],m) = (a1+a2+....+an) mod m
#               problem: too many collision 
#                                             
# 
###     Hash design - Polynomially roling hash funciton 
###     Fixed Hash Functions 
#       SHA, MDS - hash functions - adversary has prior knowledge of hash functions 
#           
###     rather than fix hash fuction - 
############################################################## 
###     Universal Hash Function 
#        1. use the chaining
#           suppose has the k serial hash function 
#                      
#
#       
#
#           
#               
#           
# 
#   
#
#
#
#
#
