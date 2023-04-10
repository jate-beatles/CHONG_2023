####################################################################
####        Binary Trees - focus on the algorithms 
#               support: insert, delete, find, sort, map, 
#               bulit the set, and dict sort of data 
#               
#               every node has 2 children, every leaf has no child call NIL
#               >IMP: Binary search tree, e1.key >= e2.key, left chil < parent < right chil 
#               > n.left is the left child 
#               > n.right is the right child
#               > n.parent is the parent
#               > n.key is the key
#               
##          Height of the BST 
#               -define count to the right/left end leaf                           
#                = max[heigh(n.legt),height(n.right)] +1 
#                if BST has the n node, how height can be?
#                 1. only has the one child in 1 direction, which can be the h = n; higly inbalanced;
#                 2. every node has each leaves, then the height can be: 
#                   = log2(n+1)   perfectly balanced 
#                 the height case         log2(n) < height < n   : big range of the height

#                
###         Find in the BST
#            > BST.find(key)  
#            initial start from the root
#             if < than thel search item, than go left, if is more >, than go right

#            def (node, key):
#               if node == NIL 
#                   return node
#               else: if (node.key == s.key) 
#                   #bingo
#                return node
#               elif node.key > s.key:
#                return find(node.left, s.key)
#               else: return find(node.right, s.key)
#               
##           COMPLEXITY OF the find on the Binary Search Trees: longest path is the height of the tree
#                                                 
#           
###         Insert the Key, just small modification of the search, insert the ele into the top of the find() 
#
###         Delete
#               1. if the find() is there, and the left and right is NIL, then the 
#               2. if the leaf is not both NIL, >>>node.left ==NIL, node.right != NIL
#                  node.right.parent = node.parent  #bypass the node
#                  if node = node. parent.left   
#                     node.parent.left = node.right
#                  else: 
#                   node.parent.right = node.right
#               3. if the delete node has 2 cholrens non-NIL
#                 > find the success of the node, > go the right of the node 1 step, then go the left to the NILL which is the succession of the NIL 
#                 - replace the successor, delete the successor 
##            Complexity of the successor, theta of h; hegiht of the tree is very vital 
#            
###         Tree Travessals 
#            -visitor partern visit very node in specific order and do something "operation"
#            inorder/preorder/postorder 
#            1.inorder - first left, then me, then right -  (node.left) then print then inoder (node.right)
#            2.preorder - first me, then left, then right - recusive
#            3.Postorder - first left, then right, last me;
#            complexity of the travessal which is 3n  theta(n)

#                                                     
####        Red-Black Trees Basics 
#             for the BST, the most often performance - find/insert/delete
#              if inser t 1,2,3,....n, the height of the tree goes as n, bad scnaria 
#              if the insert 1,2,3,....n, the height of the trees goes as log2(n), good scanria 
#            >>> 2-3 trees >>> AVL trees >> Treeps >> Skip limit
###            extra staff of the BST 
#              sitll follow the BST priciple 
#           Rule:
#            >1. rood and leaves NIL are black
#            >2. every red node must have black children 
#            >3. black height is well defined, number of black childrean on any part from any node to a leaf must be the same
#            
#               Any RBT   the heigt of the h is:
#                   log2(n)  <= h <= 2log2(n+1)
#                
#
####       Operation of RBT - Insert / Find / Delete
#           same as the BST 
#           >>except the                          
#
###         RBT _ insert(key)
#            1. find(key), delete the NIL, insert the key. 
#            2. what the color of the insert(key) ? 
#               > Case.1: the parent is black, there is no red red vilation, lucky case, nothing to do.
#               > Case.2: the parent is red, there is red-red relation, unlucky, slight change, red-red violation 
#               > Case.3: the parent is red, red-red violation, ground parent, --uncle of of the node ---- re-color the tree, change the z to red and take y and uncle w black, x keep the red
#                   whatif the z is red and red, since is recusive, thus then it will solved by recusive.  
#               > Case.4: the parent is red, red-red violation, uncle w is black, peform the ROTATION 
#                   rotation the tree
#               How to remember this ? 
#                remember the principle, just need to lookup for the pyseudo code 
#               
##             
#            >>>>Tree Rotation 
#               >1. right rotation 
#               >2. left rotation
#
# 
####        Skip Lists 
#               1. Alternative binary tree data structure 
#               2. Randomaized data structure 
#               3. invented by bill pugh
#               4. find() each up layer is for the express layer, then top more layer is more express layer 
##           Example: find(), from the top layer ----not find too far---- down layer ---- then find the find() 
#               5. insert(), take a coin to toss it, if turn up head, create a insert ele in the fresh layer 
#                   while if the current layer is top layer, set it to current layer, create a node in the current layer 
#               
##           Analysis of height = geometric random variable = 1 / (1-p), avg height of the skip list 
#            Probability of exceeding at least height h with n node
#                    booles inequality: p(at heast one node exceed h) <= np^n 
#                    n = 128, c = 2, height > = 2log2(128) = 14 
#                    comparable to binary search list, bounded to log2(N) 
#                       
##          Expected Running time of Find algorithms = 4h = clog2(n)
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


#
#
         