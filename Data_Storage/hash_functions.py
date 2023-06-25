"""
This file will show implementation of computing a hash value for a given string.
Primary sources of knowledge include: 
    1) https://cp-algorithms.com/string/string-hashing.html
    2) https://www.youtube.com/watch?v=eeiSPXCzUiE
"""

def compute_string_hash(s, p=53, m=1e9+9):
    """
    Polynomial rolling hash function will be used.
    Formula: SUM(s[i] * p**i) mod m
    p = some prime number, usually 31 for lowercase inputs, 53 for both case inputs
    m = some large prime number that will approximate the collision probability (1/m)
        since it will be the array length (or h_table size) in some sense
    """
    
    hash_result = 0  # initialize the return value
    p_to_i = 1  # initialize p**i because integer overflow is possible inside loop
    for i, c in enumerate(s):
        ascii_val = ord(c)  # convert the char into a number for summation
        hash_result = (hash_result + (ascii_val * p_to_i)) % m  # prevent 'int' overflow
        p_to_i = (p_to_i * p) % m  # once again, we don't want this value to blow up

    return hash_result

