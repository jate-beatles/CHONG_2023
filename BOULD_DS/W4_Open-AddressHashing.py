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
#            