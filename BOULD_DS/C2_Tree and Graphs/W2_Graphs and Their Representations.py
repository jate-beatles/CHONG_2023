#### 
####        Panda Asian
#               
#           -what is graphs? relation of the finite set;
#           - V = {v1, v2, v3, v4}
#              find the different combination 
#              -no self loop/ Multiedge
#              -direct & undirect graph
#              undirect has two way direct
#           -compute network
#           -Ecological network
#           -Elechical circuite
#           -GOOGLE MAPS roads 
#           >>>>>>Problems
#               Tranverse problem
#               finding short problems
#               
#
###         - Complexity of the presentation - 
#           - Adjacency List Representation - represent as list - each point to its neighbor
#             k nodes, m edge - each of the node represent to its neightbor 
#               
#                 
#               
#               
####        Graph Traversa - Bread First - specify the starting point 
#               1. Traversal - vist the node in the graph in some orders 
#               2. can only visit the node once
#               3. disconnected node - visit the nodes at once
#               4. If i visit a new node, it must be along with edge starting from already visited node.
#           Travesal Eaxmple - crawling the web - don't want to visit the page duplicated - only once
#               the web is the graph - html links to each graph
#               
###         Traversal Type ---- Bread Fist Search 
#               Adjacent list - FIFO queue, - take the head of the edge out of the queue - then move forwards - 
#               Bread search: 1. starting the node; 
#                             2. queue data structure 
#                             3. for every note arrtribues 
#                  every node is the pi is the bfs parent
#                  d: depth of the nodes 
#                  visited: True / False 
#
#
##            pseudo code 
#             def bfs(G,s) ##graph ##starting node
#                   Q  = {s}  # queue
#                   s.d = 0 
#                   s.seen = True # visited 
#                   s.pi = NIL
#                   while (Q != theta)
#                    v <= dequeque(Q)
#                   for all v include ( u, G) 
#                       if (!v,seen) >>> u.d = u.d + 1 
#                                    >>> u.pi = u
#                                    >>> u.seen = true
#                                    >>> 
#               
#
####        Depth First Search (DFS) 
#                  BFS vs DFS 
#               
#
#
#
#