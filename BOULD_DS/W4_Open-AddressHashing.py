#### Hash Table 
#           why we do need this for the solution 
#           why use the chaining 
#            1. the slot occupied 
##          Solution: Place the thing in another alternative location 
##          -Probe the sequence - open address  - looking for the next slot - slot j + 1 
#            rehash the table and insert the key 
#            Probe sequence: j + 1 
#                            do not stop looking, find the alternative location for 
#            ###Quaratic Probing :   j; j^2 + a; (j^2 + a)^2 .....e.g.
##          Delete in the Open address 
#             put a mark of the slot, then the probe sequence keep moving 
#              
##             
#
####        Perfet hash and Cuckoo Hashing 
#               - already know the keys and no collision possible 
#              
###         Why the hash is not perfect? cause the collistion- universeal hash function are fixed 
##            for the universal hash families - Possibilities = 1/m  = c/m 
#             even if the average is amll, there may be large out-liers 
#             
####        Perfect Hashing 
#            - no collision 
#               K*n^2 of the slots, and if collision happens, then redo the procedures 
#            1. choose the random hash function 
#            2. hashtable with Kn^2 slots, where K = 2c
#            3. insert each key 
#            4. if fail - abort and redo the trail 
#             
#
#             
##         K*n^2 is quite wastefull - alternative 
#           create two level hash table 
#           - put new big hash table - two level 
#           - the total size of the 2 levle hastable less than C * n(j) 
#                             
####    Cuckoo Hashing 
#           Cuckoo bids kick other birds eggs 
#           
#


