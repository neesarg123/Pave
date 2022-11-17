from multipledispatch import dispatch
import math


"""
Gauss-Jordan Elimination Method

Primary Use: Solve Systems of Linear Equations (Using Matrix Representation)
Primary Function: Convert a given Matrix (denoting linear equations) into RREF

Basic Operations (that will not affect equations denoted by each row of the Matrix):
    1. You can SWAP two rows
    2. You can MULTIPLY a row by a NON-ZERO scalar
    3. Add (and hence 'subtract') a row by a scalar multiple of another row

Rules of Reduced Row Echelon Form:
    1. The first NON-ZERO value of a row MUST BE 1
    2. Given a column contains a 1, then the same column value for remaining rows MUST BE 0
    3. The leading entry of 1 of a row should be to the RIGHT of the leading entry of the previous row
    4. A row containing of all 0s MUST BE the LAST ROW (or beneath a row containing at least one non-zero entry)
"""

def rref(A):
    """
    Converts an Augmented Matrix (where last column represents systems' values) into Reduced Row Echelon Form

    :param A: 2D array representing an Augmented Matrix (m x n)
    :return: 2D array Matrix A in Reduced Row Echelon Form

    Algorithm:
    - Begin at Row, R = 0; Column, C = 0; Frontier = 0
        1. Ensure rows containing all zeros are below all other rows
        2. Swap rows such that the row with highest NON-ZERO leading entry at column C becomes row at Frontier 
        3. Multiply Frontier row with a scalar such that the NON-ZERO leading entry is 1
        4. Add (+ or -) scalar multiples of the Frontier row with all other non-zero rows (above and below Frontier) 
           such that the other column values at C are 0 wherever the leading entry of the Frontier row is 1
        5. Increment R and C and Frontier, and repeat steps 2 - 4 until R reaches len(A)
        6. Ensure the leading entry of a row is to the right of the leading entry of the previous row
    """

    zeros_to_bottom(A)
    
    frontier = 0
    col = 0

    while frontier < len(A):
        if A[frontier] != [0]*len(A[0]):
            get_top_row(A, col, frontier)
            for r in range(len(A)):
                if r != frontier:
                    reduce_row(A, r1=frontier, r2=r, column_index=col)
        frontier += 1
        col += 1

    return A


def zeros_to_bottom(A):
    """
    Ensures all zero rows are at the bottom of the Augmented Matrix A

    :param A: 2D array representing an Augmented Matrix (m x n)
    :return: A
    """

    A.sort(key=lambda x: x[:-1] == [0] * (len(x) - 1))
        
    return A


def swap(A, r1, r2):
    """
    Swaps row r1, of Augmented Matrix A with row r2

    :param A: 2D array representing an Augmented Matrix (m x n)
    :param r1: integer representing a row contained in A
    :param r2: integer representing a row contained in A
    :return: A
    """

    temp = A[r1]
    A[r1] = A[r2]
    A[r2] = temp

    return A


def get_top_row(A, column_index, frontier_row=0):
    """
    Swap rows such that the row with highest NON-ZERO leading entry at given column is the Frontier row
    
    :param A: 2D array representing an Augmented Matrix (m x n)
    :param column_index: integer representing which column to find maximum value
    :frontier_row: defaults to 0, indicating first row is the starting Frontier row
    :return: A
    """

    max_column_value = max_row_id = -math.inf

    for row_idx, row in enumerate(A):
        if row_idx >= frontier_row:
            if abs(row[column_index]) > max_column_value:
                max_column_value = row[column_index]
                max_row_id = row_idx
    swap(A, r1=frontier_row, r2=max_row_id)

    return A


@dispatch(list, int)
def find_leading_entry(A, r):
    """
    Finds the value and column index of the first NON-ZERO entry in a given row of the Augmented Matrix A

    :param A: 2D array representing an Augmented Matrix (m x n)
    :param r: integer representing a row of A
    :return: dict containing integer value and column index of the first NON-ZERO value in the given row of A
    """

    for col_ix, col_val in enumerate(A[r][:-1]):
        if col_val != 0:
            return {'value': col_val, 'col_idx': col_ix}

    return {'col_idx': float('inf')}


@dispatch(list)
def find_leading_entry(r):
    """
    Finds the value and column index of the first NON-ZERO entry in a given row (list)

    :param r: list representing a row of some Matrix
    :return: dict containing integer value and column index of the first NON-ZERO value in the given row
    """

    for col_ix, col_val in enumerate(r[:-1]):
        if col_val != 0:
            return {'value': col_val, 'col_idx': col_ix}
    
    return {'col_idx': float('inf')}


def multiply_row(A, r, s):
    """
    Multiplies a given row r of Augmented Matrix A with given scalar value s

    :param A: 2D array representing an Augmented Matrix (m x n)
    :param r: integer representing a row of A
    :param s: integer scalar value representing the multiplier
    :return: list of integers representing the multiplication of a row by some scalar
    """

    return [curr_val * s for curr_val in A[r]]


@dispatch(list, int, int)
def add_two_rows(A, r1, r2):
    """
    Adds two given rows of the Augmented Matrix A

    :param A: 2D array representing an Augmented Matrix (m x n)
    :param r1: integer representing row of A
    :param r2: integer representing row of A
    :return: list of integers representing the addition of two rows of A
    """

    return [val_r1 + val_r2 for val_r1, val_r2 in zip(A[r1], A[r2])]


@dispatch(list, list, int)
def add_two_rows(A, row, r2):
    """
    Adds a given row to a specified row in the Matrix A

    :param A: 2D array representing an Augmented Matrix (m x n)
    :param row: list of integers containing n elements
    :param r2: integer representing row of A
    :return: list of integers representing the addition of tow rows of A
    """

    return [val_r1 + val_r2 for val_r1, val_r2 in zip(row, A[r2])]

    
def sort_rows(A):
    """
    Sorts the rows of Augmented Matrix A such that NON-ZERO leading entry of each row is to the right
    of the NON-ZERO leading entry of the row above it

    :param A: 2D array representing an Augmented Matrix (m x n)
    :return: A
    """
    
    A.sort(key=lambda x: find_leading_entry(x)['col_idx'])

    return A


def reduce_row(A, r1, r2, column_index):
    """
    Given two rows of Augmented Matrix A, reduce row #2 using row #1 such that a given column of row #2
    becomes 0.

    :param A: 2D array representing an Augmented Matrix (m x n)
    :param r1: integer, first row, the reference row
    :param r2: integer, second row, on which to perform operations
    :param column_index: integer, the column of r2 that needs to be 0
    :return: A
    """
    # first, we simply r1 by multiplying it by 1 / r1[column_index]
    if A[r1][column_index] != 0:
        A[r1] = multiply_row(A, r1, 1 / A[r1][column_index])
        # now that r1 is scaled properly, we multiply it with -r2[column_index]
        sub_r1 = multiply_row(A, r1, -A[r2][column_index])
        # finally, we add the negatively weighted r1 with r2
        A[r2] = add_two_rows(A, sub_r1, r2)

    return A

