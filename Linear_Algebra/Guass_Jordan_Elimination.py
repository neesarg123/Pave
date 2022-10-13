from multipledispatch import dispatch


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
        1. Ensure rows containing all zeros are below all other rows
        2. Swap rows such that the row with highest NON-ZERO leading entry is the 1st row
        3. Multiply 1st row with a scalar such that the NON-ZERO leading entry is 1
        4. Add (+ or -) scalar multiples of the 1st row with all other non-zero rows such that the other column values
           are 0 wherever the leading entry of the 1st row is 1
        5. Repeat steps 2-4 until the leading entries of all non-zero rows is 1
        6. Ensure the leading entry of a row is to the right of the leading entry of the previous row
    """
    
    zeros_to_bottom(A)
    while not check_all_leading_entries_one(A):
        bubble_up_highest_leading_entry(A)
        leading_entry_first_row = find_leading_entry(A, 0)
        A[0] = multiply_row(A, 0, 1 / leading_entry_first_row['value'])
        # TODO: step 4
        # Find the column index  
        leading_entry_col_idx = leading_entry_first_row['col_idx']
        # At that column index, every row (except for row 0) value needs to be 0
        # Multiply row 0 with (-) leading entry of every other row
        # Add the above multiple of row 0 with each corresponding row 
    return A


def zeros_to_bottom(A):
    """
    Ensures all zero rows are at the bottom of the Augmented Matrix A

    :param A: 2D array representing an Augmented Matrix (m x n)
    :return: A
    """

    A.sort(key=lambda x: x == [0]*len(x))
        

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


@dispatch(list, int)
def find_leading_entry(A, r):
    """
    Finds the value and column index of the first NON-ZERO entry in a given row of the Augmented Matrix A

    :param A: 2D array representing an Augmented Matrix (m x n)
    :param r: integer representing a row of A
    :return: dict containing integer value and column index of the first NON-ZERO value in the given row of A
    """

    for col_ix, col_val in enumerate(A[r]):
        if col_val != 0:
            return {'value': col_val, 'col_idx': col_ix}

    return {}


@dispatch(list)
def find_leading_entry(r):
    """
    Finds the value and column index of the first NON-ZERO entry in a given row (list)

    :param r: list representing a row of some Matrix
    :return: dict containing integer value and column index of the first NON-ZERO value in the given row
    """

    for col_ix, col_val in enumerate(r):
        if col_val != 0:
            return {'value': col_val, 'col_idx': col_ix}
    
    return {}


def bubble_up_highest_leading_entry(A):
    """
    Places row with the highest leading entry to the very top of the Augmented Matrix A

    :param A: 2D array representing an Augmented Matrix (m x n)
    :return: A
    """

    max_leading_entry = find_leading_entry(A, 0)['value']
    max_leading_entry_rid = 0
    for rid, row in enumerate(A):
        row_le = find_leading_entry(row)
        if row_le['value'] > max_leading_entry:
            max_leading_entry = row_le['value']
            max_leading_entry_rid = rid

    swap(A, r1=0, r2=max_leading_entry_rid)
    
    return A


def multiply_row(A, r, s):
    """
    Multiplies a given row r of Augmented Matrix A with given scalar value s

    :param A: 2D array representing an Augmented Matrix (m x n)
    :param r: integer representing a row of A
    :param s: integer scalar value representing the multiplier
    :return: list of integers representing the multiplication of a row by some scalar
    """

    return [curr_val * s for curr_val in A[r]]


def add_two_rows(A, r1, r2):
    """
    Adds two given rows of the Augmented Matrix A

    :param A: 2D array representing an Augmented Matrix (m x n)
    :param r1: integer representing row of A
    :param r2: integer representing row of A
    :return: list of integers representing the addition of two rows of A
    """

    return [val_r1 + val_r2 for val_r1, val_r2 in zip(A[r1], A[r2])]


def check_all_leading_entries_one(A):
    """
    Determines whether all NON-ZERO rows' leading entry is 1

    :param A: 2D array representing an Augmented Matrix (m x n)
    :return: True or False
    """

    for row in A:
        if find_leading_entry(row)['value'] != 1:
            return False
    return True

    
def sort_rows(A):
    """
    Sorts the rows of Augmented Matrix A such that NON-ZERO leading entry of each row is to the right
    of the NON-ZERO leading entry of the row above it

    :param A: 2D array representing an Augmented Matrix (m x n)
    :return: A
    """
    
    A.sort(key=lambda x: find_leading_entry(x)['col_idx'])

    return A

