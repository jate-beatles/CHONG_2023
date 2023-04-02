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
#
#
#


#
#
         