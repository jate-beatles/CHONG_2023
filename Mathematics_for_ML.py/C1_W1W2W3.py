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
#   0 1    called to flip the x-axis cordinator 90 degree [anti-clock wise direction]
##
#   -1 0 
#    0 -1   called to flip both asix cordinator [x-axis turn 90, and y-axis turn 90]
##
#    0 1 
#    1 0    called to put a mirror based on 45 degree
##   
#    0 -1 
#    -1 0   called to put the mirror in aonther -45 degree
##
#    -1 0 
#     0 1    called to put vertical mirror 
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
#########################################################################
#### Composition or combination of matirs transformations 
##
#     A1 to A2 to A3 is Associative     
#     but not --- cannot change the order ---- commutative
#     
##########################################################################
#### Solving the problems - Gaussian elimination 
#   find the inverse of the to find the A 
#   A^-1 . A = I 
#   find the A inverse
#
#   eliminate the diagnose 0 of the matrix 
#   to find the 100
#             010
#             001
#       elimination, back substitution up of the solution
####  form Gaussian elimination to finding the inveser
#      B = A ^(-1)   by the eliminate the decompisition of the matrix, to find the inverse
# 
#
##################################################################################
####  Determinants and inverses 
####  Detereminants is the area of the matirix, if the determinant is 0, then no solution
# #      the matirx collapase in 2d space

""" 
A[0, 0]  A[0, 1]  A[0, 2]  A[0, 3]
A[1, 0]  A[1, 1]  A[1, 2]  A[1, 3]
A[2, 0]  A[2, 1]  A[2, 2]  A[2, 3]
A[3, 0]  A[3, 1]  A[3, 2]  A[3, 3] """
import numpy as np 

def isSingular(A): 
    B = np.array(A,dtype=np.float_)
    try:
        fixRowZero(B)
        fixRowOne(B)
        fixRowTwo(B)
        fixRowThree(B)
    except MatrixIsSingular: 
        return True
    return False

class MatrixIsSingular(Exception): pass

def fixRowZero(A) :
    if A[0,0] == 0 :
        A[0] = A[0] + A[1]
    if A[0,0] == 0 :
        A[0] = A[0] + A[2]
    if A[0,0] == 0 :
        A[0] = A[0] + A[3]
    if A[0,0] == 0 :
        raise MatrixIsSingular()
    A[0] = A[0] / A[0,0]
    return A

def fixRowOne(A) :
    A[1] = A[1] - A[1,0] * A[0]
    if A[1,1] == 0 :
        A[1] = A[1] + A[2]
        A[1] = A[1] - A[1,0] * A[0]
    if A[1,1] == 0 :
        A[1] = A[1] + A[3]
        A[1] = A[1] - A[1,0] * A[0]
    if A[1,1] == 0 :
        raise MatrixIsSingular()
    A[1] = A[1] / A[1,1]
    return A

def fixRowTwo(A) :

    A[2] = A[2] - A[2,0]*A[0]
    A[2] = A[2] - A[2,1]*A[1]

    if A[2,2] == 0 :
        A[2]= A[2] + A[3]
        A[2] = A[2] - A[2,0]*A[0]
        A[2] = A[2] - A[2,1]*A[1]

    if A[2,2] == 0 :
        raise MatrixIsSingular()
    
    A[2] = A[2] / A[2,2]
    return A

def fixRowThree(A) :

    A[3] = A[3] - A[3,0]*A[0]
    A[3] = A[3] - A[3,1]*A[1]
    A[3] = A[3] - A[3,2]*A[2]

    if A[3,3] == 0: 
        A[3] = A[3] + A[2]
        A[2] = A[2] - A[2,0]*A[0]
        A[2] = A[2] - A[2,1]*A[1]    
    if :
        raise MatrixIsSingular()
    
    return A
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
#########################################################################################################
#########################################################################################################
############ W4 Matirx make linear Mapping

#### Einstein Summatoin 
##
#### for each element, a ij, i is the row, and the j is the column number
#       (ab).23   = a 2 row * b 3 column 
#
#     if the summation convetion is for coding 
#       AB = C 
#       Cik = a(ij) b(jk)              the a column number should == row of the b
#       
#       
#### Matix changin basis
#      changing the frame of the matrix from A to B frame
#       how to inverser the marix back? B^-1
#       
#            
#
#




