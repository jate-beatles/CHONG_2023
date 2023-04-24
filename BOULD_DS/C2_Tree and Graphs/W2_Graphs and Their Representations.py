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
#            continue visit the succuss of the node, then return
#            
###         pseudo code 
#           def visit(G,v) 
#              ##global time = 1 
#              v(pi = parent; d = discovery time[undifined]; f = finish time;)
#              ##Book Keeping 
#               if (v.seen): 
#                return
#               for all v in adjacent ( v) 
#                   if(not v. seen):
#                    v.seen = True
#                    v.pin = v
#3                   v.d = time
#                     time += 1 
####                dfs visit (G,v)
#           time = time + 1 
#           v.f = time
#           
####        1. when dfs running, it creas dfs tree 
#           2. some of edge: 
#               > back edge - back to the ancestor of the node
#               > cross edge - sibling 
#               > forward edge - go form the ancestor not directe child of the tree 
#           
####        DFS example 
#           
#           run the outer loop: 
#               for i = 1 to n: # n = all nodes
#                   dfs visit(G,i)
#           dfs visit do not return a tree, which will show the edges 
#           
####        Back Edges -- Desc tp the ancestor nodes
#           Foward Edges -- anscendant to the nodes not his child
#           Cross Edge -- sibling child cross
###        Find the edge by the discovery time and finish time 
#           --Back edge:  v.d < u.d < u.f < v.f  [ u back to v]
#           --Forward edge: u.d < v.d < v.f < u.f  [v back to u] u forward to v
#           --Cross edge: 

###         The edge for usefull for the problem: 
#               if the graph has the circle: 
#                back edge = cycle?? every back edge will for create a cycle. 
#               
#                
#                         
#
####        Topological Sort
#           DAG -  direcrted acyclic graph 
#            tasks for hte each v_1, v_2, v_3, 
#             >>>  v_2 only start when the v_1 finish ...., edge call as dependences 
#             >>> sor the graph 
#             >>> the v_1 > v_2 ....>v_6   call as the topologicdal sort 
#            [direct acyclic graph] 
#            
#           1. DFS
#           2. sort the order in the descending order
#           3. dfs - finish step then, put the node as the descending order
#           4. back edge has no Topologicdal sort ----- circle 
#           visit every node, total time = theta (|v| + |f|)
#               