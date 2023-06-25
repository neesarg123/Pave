import math

def _gen_next_prime(curr_prime):
    """
    This function returns the next prime number greater than the given prime number.
    """
    def _is_prime(number):
        for i in range(2, int(math.sqrt(number)) + 1):  # check 2 to sqrt(n)
           if number % i == 0:
               return False
        return True

    number = curr_prime + 1
    while True:
        if _is_prime(number):
            return number
        number += 1

