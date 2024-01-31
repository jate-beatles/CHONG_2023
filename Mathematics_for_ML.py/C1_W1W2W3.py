###Course 1  - linear regression 

##For the gaussan distributione 
# f(x) - 1/segea(2pi)^1/2 + exp{-(x-u)^2 / (2segma^2)}
## Operation with the vector
###  associative vector: 
#               r + s = s + r   (components add to components)
#               -(s) = - for(s1, s2)  for each components 
#                  
#### Modulus & inner product 
# r = [ri, rj]  s = [si, sj]

############################################################################
### THE LENGTH OF THE VECTOR = THE SIZE OF THE VECTOR 
### THE DOT PRODUCT OF THE VECTOR = THE INNER SCALAR   //// PRJECTION PRODUCTION 
### THE DOT PRODUCT OF THE VECTOR ITSELF THEN ^1/2 get the size 

# the length of the r = (a^2 + b^2)^(1/2)
##### Commutative  r . s = s. r = ri*si + rj * sj
##### Distributive over addition: r .(s+t) = r.s + r.t
##### Associatie over scalar multiplication: r.(as) = a(r.s)  ##a is the multiple scalar number
##### if vector length is the multiply its self
################    r.r = r1.r1 + r2.r2 = r1^2 + r2^2 = |r|^2

#############################################################################
#### cosince rules  c^2 = a^2 + b^2 - 2abcos(theta)
#                   |r-s|^2 = |r|^2 + |s|^2 - 2|r||s|cos(theta)
# we can use the vector to figure out by using cot product vecto it self then ^1/2 to get the size of the vectors
#                   |r-s|^2 = (r-s).(r-s) = r.r -s.r - s.r + s.s
#         |r|^2 - 2r.s + |s|^2 =  |r|^2 + |s|^2 - 2|r||s| cos(theta)
#       r.s = |r| . |s| . cos(theta)
#       if the cosine is 90 degree, then cos(90) is 0, the r.s is the 0
#       if the cosine is 180 degree, then cos(180) is -1, the r.s will be -|s||r| 
#
#     
######################################################################
#### Projection
#    r.s = |r||s|* cos(theta)
#        |s|*cos(theta)   is the shadow of the size s on the r 
#        the dot of production is the size of |r| * projection of the |s| on the the |r| 
#        
#     r.s / |r|  = |s| cos(theta)     SCALAR PROJECTION
#### The vector projection ---------r.r = |r||r|  ---is a number * length of r
###########    r.s/ |r||r| = r.s / r.r ################
###########   vector projection = r. [(r.s) / |r||r|]   ####The unit vector projection



#####################################################################
#### Changing BASIS
#    the basis vector to describe the any vector
#       the big if ==orthogonal== check whether the basis vector is 90 degree  cos(theta)  = b1.b2/|b1||b2|  = 0 
#       but we also could use the matirx to find the vector b1, and b2
#        1. using the dot product to chech basis vector is 90 degree
#        2. find the vector projection ===== re.b/|b|^2
#        3. find the vector projection for each basis 
#        4. rb = [r.b1 / |b1|^2].b1 + [r.b2/|b2|^2].b2
#        
#    
#####################################################################
####  Basis - set of n vectors (i) not linear combinations each other linearly independent
#                              b3 != a1b1 + a2b2
#                              (ii)span the space
#                               (iii)the space is n-dimensional
#
####  The applications of changing basis
#     


########################################################################
######################################################################
#### Week 3 ####
#### Matrices, vectors and solving simutaneous equation problems
#   
#### Matrix transform space
#       Matrix  A,  the transform as the r
#       then the vector:  A(nr) = nr'
#                         A(r+s) = Ar + As 
#                         A(re1' + me2')
#  any vector could be express by the element vector, the n
#  the matrix of the n vector change the transform, to get the new vector
#                           
#### Type of matirx transformation 
#  1 0
#  0 1    called as identity matirx
##
#  3 0 
#  0 2    called as the scaled matrix
##
#  -1 0 
#   0 1    called to flip the x-axis cordinator 90 degree
##
#   -1 0 
#    0 -1   called to flip both asix cordinator
##
#    0 1 
#    1 0    called to put a mirror in 45 degree
##   
#    0 -1 
#    -1 0   called to put the mirror in aonther 45 degree
##
#    -1 0 
#     0 1    called to put vertical mirror 
#
## 
#     1 0 
#     0 -1    called to put the horizantal mirror 
##
#     1 1 
#     0 1     called to shear the x-axis to right 1 
##
#     0 -1 
#     1  0    called to rotate the vector 
#
#




#### Linear Algebra 

##          The size for the vector is the square root of hte sum of the ###squares of its compoments

###### a. b= a1*b1 + a2*b2 + .... + an*bn 
### Projection is the S onto R, the shadow length of the projection 
#   
#
#   r.s = |r| * |s| * cos(theta)  >>>> theta is the angle between r and s 
#
#
#   (r.s)/|r| = |s|* cos(theta)   >>> right part is the scalar project 
#
##### Projection:    the sca  (r.e) / |e|^2 
#####  Changing Basis 
#
# change the vector basis using other vector - simply understand process by the angle is 90 degree 
#

####  Basis & Vector the linear independece 
#       b3 != a* b2 + c * b1   there are linear combinations 
#       
#
# Nothing updated  refer to this modules 
#






