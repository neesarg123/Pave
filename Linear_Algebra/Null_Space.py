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

from Guass_Jordan_Elimination import rref, print_result
from fractions import Fraction 


def null_space(A, verbose=True):
    """
    Finds the Null Space of Matrix A
    
    :param A: 2D array representing a Matrix (m x n)
    :return: Set of vectors representing the Null Space
    """
    
    rref_a = rref(A)
    print_result(rref_a)
    
    pivot_cols = []
    non_pivot_cols = []

    for col in range(len(A[0])):
        col_row = get_column(A, col)

        # if the number of 0's in that column is less than the number of rows - 1
        if col_row.count(0) == len(A) - 1:  
            pivot_cols.append(col)  # then it's a pivot column 
        else: 
            non_pivot_cols.append(col)  # otherwise, it's a non-pivot column

    print(pivot_cols)
    print(non_pivot_cols)


def get_column(A, c):
    """
    Returns the column values for all rows of a Matrix A

    :param A: 2D array representing a Matrix (m x n)
    :param c: Column number to extract
    """

    return [row[c] for row in A]


A = [[Fraction(1, 1), Fraction(1, 1), Fraction(1, 1), Fraction(1, 1)], [Fraction(2, 1), Fraction(1, 1), Fraction(4, 1), Fraction(3, 1)],
        [Fraction(3, 1), Fraction(4, 1), Fraction(1, 1), Fraction(2, 1)]]
null_space(A)

