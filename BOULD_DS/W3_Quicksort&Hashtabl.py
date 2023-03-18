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
#           Lomuto Partition - italiy science 
#           THE ARRAY REARRANGEMENT IS IN PLACE, in the intermediate steps: 
#           1. A: [ ..........x] - divide into 3 regions
#              the whole region is unprocess at the beginning  
#           2. everything in region1 is less than the pivo, region2 greater than pivot,
#              then, last region is the unprocess region
#              the region1 less then the pivot 
#           3. swap the ele in the region1 a[i+1] swap with the a[j] if a[j] < x<  
#              then the entire: 
#           while (j < n-1) : 
#               if A[j] < x: 
#               initially region1 and region2 is empty, i = 0, j = 1 
#               everything is unprocess
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
