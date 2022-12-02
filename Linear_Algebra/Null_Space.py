"""
Null Space: 
    Of a matrix, A, defines the set of vectors, N, that satisfy the condition:
        A (x) Ni = The ZERO vector for 'i' in N

Implications of Null Space:
    If the set N = {The ZERO vector}, then Column Space of A is Linearly Independent
    Otherwise, the Column Space of A is Linearly Dependent

High-Level Algorithm:
    The Null Space of A is equivalent to the Null Space of RREF(A)
    Determine pivot rows of RREF(A),
        If all columns are pivot, then we reach L.I.
        Otherwise, find the non-pivot columns
"""

from Guass_Jordan_Elimination import rref 


def null_space(A, verbose=True):
    """
    Finds the Null Space of Matrix A
    
    :param A: 2D array representing a Matrix (m x n)
    :return: Set of vectors representing the Null Space
    """
    
    print(rref(A))


A = [[1, 1, 1, 1], [2, 1, 4, 3], [3, 4, 1, 2]]
null_space(A)

