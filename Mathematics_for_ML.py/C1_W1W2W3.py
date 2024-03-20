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

# """ 
# A[0, 0]  A[0, 1]  A[0, 2]  A[0, 3]
# A[1, 0]  A[1, 1]  A[1, 2]  A[1, 3]
# A[2, 0]  A[2, 1]  A[2, 2]  A[2, 3]
# A[3, 0]  A[3, 1]  A[3, 2]  A[3, 3] """
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

# def fixRowThree(A) :

#     A[3] = A[3] - A[3,0]*A[0]
#     A[3] = A[3] - A[3,1]*A[1]
#     A[3] = A[3] - A[3,2]*A[2]

#     if A[3,3] == 0: 
#         A[3] = A[3] + A[2]
#         A[2] = A[2] - A[2,0]*A[0]
#         A[2] = A[2] - A[2,1]*A[1]    
#     if :
#         raise MatrixIsSingular()
    
#     return A
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
#       Bear basis vector in my basis world matrix :
#       [3,1]
#       [1,1] 
#       find the B^-1 of to reverse the bear basis
#       1/2 * [1, -1]     
#             [-1, 3]       my basis in bear world 
#   
#       
#### Using the projection - vector module could be use the prjection to the point
#      using the that projection to changing should be orthogonal
####    Doing the transformation in a changed basis 
####    change the basis rotation
#       
#       [3, 1]
#       [1, 1]
#           
#       the rotation basis of 45 degree in my basis:
#       1/2^(1/2) [1, -1]
#                 [1, 1]
#     so the flow as below: 
#    B^-1  * Roration * Bear Basis * [vector] 
#       
#       
#### Orthogonal Matrices 
#       transpose A is the A[T]ij  = Aji 
#          [1,2]                [1,3]
#          [3,4]   transpose    [2,4]
#
#       A(T). A is the n*n identical matrix
#       A(T) = A^(-1) 
#       A(T) . A = I 
#       
#
#### The gram-schmidt process 
#
#       built the thorogonal matrix 
#       v1 set - e1 is the normalize vision of v1 
#       
#       v2 = projection to e1 on the direction of v1 + u2  which is orthogonal to e1 

########################################################################################
########################################################################################
#Gram-schmidt Process 
#   v = [v1, v2, ...vn]
#### Step1: e1 = v1 / |v1|  which is normalised v1 as the basis 
#### Step2: v2 = (v2.e1). e1 /|e1| + u2  whici u2 is the orthogonal component of basis to e1
#      find the u2 = v2 - (v2.e1)e1, then standilze u2 find the e2
# 
#### Step3: u3 =  v3 - (v3.e1)e1 - (v3.e2)e2 which u3 is the perpendicular to the plane of e1 * e2
#     [perpendicular to e1 & e2 plance]
#     then nomalized u3 to get the e3, 
#     find the all unit vectors e1, e2, e3
'''
A[0, 0]  A[0, 1]  A[0, 2]  A[0, 3]
A[1, 0]  A[1, 1]  A[1, 2]  A[1, 3]
A[2, 0]  A[2, 1]  A[2, 2]  A[2, 3]
A[3, 0]  A[3, 1]  A[3, 2]  A[3, 3]
'''
# the dot production in numpy
#u @ v
import numpy as np
import numpy.linalg as la

verySmallNumber = 1e-14 # That's 1×10⁻¹⁴ = 0.00000000000001

def gsBasis4(A) :
    B = np.array(A, dtype=np.float_)
    ### COLUMN 0 TO NOMALIZE
    B[:, 0] = B[:, 0] / la.norm(B[:, 0])

    ### get the u1 
    B[:, 1] = B[:, 1] - B[:, 1] @ B[:, 0] * B[:, 0]

    ### normalise the u2 to get the e1
    if la.norm(B[:, 1]) > verySmallNumber :
        B[:, 1] = B[:, 1] / la.norm(B[:, 1])
    else :
        B[:, 1] = np.zeros_like(B[:, 1])

    ### get the u2 & nomalise u2 to get the e2
    B[:,2] = B[:,2] - B[:,2]@B[:,0]*B[:,0] - B[:,2]@B[:,1]*B[:,1]
    if la.norm(B[:, 2]) > verySmallNumber :
        B[:, 2] = B[:, 2] / la.norm(B[:, 2])
    else :
        B[:, 2] = np.zeros_like(B[:, 2])  

    ### get the u3 & normalized u3 to get the e3
    B[:,3] = B[:,3] - B[:,3]@B[:,0]*B[:,0] - B[:,3]@B[:,1]*B[:,1] - B[:,3]@B[:,2]*B[:,2]
    if la.norm(B[:, 3]) > verySmallNumber :
        B[:, 3] = B[:, 3] / la.norm(B[:, 3])
    else :
        B[:, 3] = np.zeros_like(B[:, 3]) 
# 
#    # Finally, we return the result:
    return B
        
def gsBasis(A) :
    B = np.array(A, dtype=np.float_) # Make B as a copy of A, since we're going to alter it's values.
    # Loop over all vectors, starting with zero, label them with i
    for i in range(B.shape[1]) :
        # Inside that loop, loop over all previous vectors, j, to subtract.
        for j in range(i) :
            # Complete the code to subtract the overlap with previous vectors.
            # you'll need the current vector B[:, i] and a previous vector B[:, j]
            B[:, i] = B[:,i] - B[:,i]@B[:,j]*B[:,j]
        # Next insert code to do the normalisation test for B[:, i]
        if la.norm(B[:, i]) > verySmallNumber :
            B[:, i] = B[:, i] / la.norm(B[:, i])
    # Finally, we return the result:
    return B

# This function uses the Gram-schmidt process to calculate the dimension
# spanned by a list of vectors.
# Since each vector is normalised to one, or is zero,
# the sum of all the norms will be the dimension.
def dimensions(A) :
    return np.sum(la.norm(gsBasis(A), axis=0))

'''
V = np.array([[1,0,2,6],
              [0,1,8,2],
              [2,8,3,1],
              [1,-6,2,3]], dtype=np.float_)
gsBasis4(V)

B = np.array([[6,2,1,7,5],
              [2,8,5,-4,1],
              [1,-6,3,2,8]], dtype=np.float_)
gsBasis(B)
'''

########################################################################################
########################################################################################
#Reflecting in a plane
##

#T=E*Te*E−1

#  a=s⋅t     M = A @ B
#
# inv(A)
# transpose(A)
# gsBasis(A)

import numpy as np
from numpy.linalg import norm, inv
from numpy import transpose
from readonly.bearNecessities import *





              



