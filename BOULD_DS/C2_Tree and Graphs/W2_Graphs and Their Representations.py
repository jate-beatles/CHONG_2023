#### 
####        Panda Asian
#               
#           -what is graphs? relation of the finite set;
#           - V = {v1, v2, v3, v4}
#              find the different combination 
#              -no self loop/ Multiedge relate to same nodes 
#              -direct & undirect graph(bidirectional)
#              undirect has two way direct

#           Why do the graph comes from?  
#           -compute network  - node is servers - edge is the link
#           -Ecological network  - node is people - edge is the network
#           -Elechical circuite  - node is species  - edge is relation 
#           -GOOGLE MAPS roads  - 
#           >>>>>>Problems
#               Tranverse problem
#               finding short spots problems
#               finding the spainning trees
#               finding the flow
#
#           How to present the graph - 
###         - Complexity of the presentation - 
#           - Simple way to present the matrix - Adjacency List Representation - represent as list - each point to its neighbor
#             k nodes, m edge - each of the node represent to its neightbor [less contains the 0 than adjacnecy list]
#             
#                  
###############################################################################             
####        Graph Traversa - Bread First - specify the starting point - Short Spot Search 
#               1. Traversal - vist the node in the graph in some orders 
#               2. can only visit the node once
#               3. disconnected node - visit the nodes at once
#               4. If i visit a new node, it must be along with edge starting from already visited node.
#           Travesal Eaxmple - Business Case -  crawling the web - don't want to visit the page duplicated - only once
#               the web is the graph - html links to each graph
#               
###         Traversal Type ---- Bread Fist Search - FIFO data structure 
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
#             >>> sort the graph 
#             >>> the v_1 > v_2 ....>v_6   call as the topologicdal sort 
#            [direct acyclic graph] 
#            
#           1. DFS
#           2. sort the order in the descending order
#           3. dfs - finish step then, put the node as the descending order
#           4. back edge has no Topologicdal sort ----- circle 
#           visit every node, total time = theta (|v| + |f|)
#               

####
####        SCC - Strongly Constucted Component
#              1. a subset of the vertices
#              2. the path must entire lie inside - every node to every node
#              3. circle should also be the SCC 
#              4. Maximal strongly connected components 
#   
####       SCC - strongly connected components  - Properties 
#           >>>1. If the Maximal Strongly Connected components MSCC - 2 different components 
#             s1 union with s2, is a large scc containing s1 and s2, - therefore s1 and s2 cannot be maximal and s2 cannot be maxiaml connected conponents 
#               in many books the notation scc is mscc, while in this lecture, MSCC only is the MSCC
#         
#           >>>2. Supper Graph - take MSCC into a node by itself - and add connection across the SCC
#                 new edge - MSCC supper graph - MSCC supper graph cannot have circle - 
#                 - MSCC
#           >>>3. The reverse graph, G has the same MSCC as the original 
#                 - revere the direction of every edge
#                 - 
####        SCC - Algorithm - for finding the maximal strongly connected components 
#                1. do the DFS on the G^T reverse the G
#                   DFS on the origin node >>>> then DFS on the reverse graph
#                   ----keep the list of the finish time of the DFS on the G ----
#                   DFS on the reverse G - descending order of the finish time - each element settle as the order 
#                   DFS REVERSE - DFS visit is start then only visit it self - then you will print tjhe MSCC in the list
#                    - then dfs search as :  {1} {2, 5, 4,3}, remove the node from the reverse list 
#                      print out the MSCC - your will end up to print the MSCC of the DFS on the reverser G
#
###        Why Algorithm works 1. Supper graph is DAG
#                              2. Supper graph exist, and the reverse graph has the same MSCC as the origin MSCC 
#                              3. Topological super graph, then the circle in it 
#                              4. The SCC connect with another SCC, then become a MSCC 
#                               
###       Do some shit things, you do not to wait for anything is ready for you, never ready for you 
#         go go go, rush into the dust, dark and the mist field, fuck it our chong chong chong       