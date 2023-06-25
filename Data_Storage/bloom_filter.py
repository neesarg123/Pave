from hash_functions import compute_string_hash
from helper import _gen_next_prime
import math

"""
This file contains implementation of creating a bloom filter of a given size.
It also includes functionality to add values into the bloom filter and search membership.
Moreover, you can find a method that can determine the optimal size of your filter given
relevant parameters.
"""

class BloomFilter:
    def __init__(self, size=1000, number_of_hash_functions=1):
        self.size = size
        self.number_of_hash_functions = number_of_hash_functions
        self.bit_array = [0] * size  # initialize a bit array of length size and all 0s


    def add_string(self, s):
        p = 53
        for i in range(self.number_of_hash_functions):
            index = compute_string_hash(s=s, p=p, m=self.size) 
            # set the bit at the obtained index to 1 to mark membership
            self.bit_array[index] = 1
            # no need to compute the next line if num of hash is 1
            if self.number_of_hash_functions > 1:
                # change p to be the next prime number so the hash value changes
                p = _gen_next_prime(p)
            

    def check_membership(self, s):
        p = 53
        for i in range(self.number_of_hash_functions):
            # check if hashed index is set to 1
            index = compute_string_hash(s=s, p=p, m=self.size)
            # now check if the bit was set to 1 at the index
            if self.bit_array[index] == 0:
                return False
            # change p to be the next prime number so the hash value changes
            p = _gen_next_prime(p)
        return True


    def __str__(self):
        result = "Bloom Filter Size: " + str(self.size) + "\nNumber of Hash Functions: " + str(self.number_of_hash_functions)

        result += "\nBit Array:\n" + str(self.bit_array)

        return result


def get_optim_bloom_filter_size(number_of_anticipated_elements, desired_false_positive_rate):
    """
    Bloom Filters are typically created much smaller than the number of expected elements
    to be queried for membership.
    Note: false positive rate must be less than or equal to 1.
    """
    assert desired_false_positive_rate <= 1, "false positive rate cannot exceed 1"
    assert desired_false_positive_rate > 0, "false positive rate must be positive"

    n = number_of_anticipated_elements
    f = desired_false_positive_rate

    return math.ceil((n * math.log(f)) / math.log(1 / (2**math.log(2))))


def get_optim_num_of_hash_functs(filter_size, number_of_anticipated_elements):
    """
    Having more hash functions can reduce the false positive rate in practice.
    """

    m = filter_size
    n = number_of_anticipated_elements

    return round(math.log(2) * m / n)


input_strings = ["nee", "vee", "wowzers", "gilu", "nisu", "visu", "kalu"]

bloom_filter1 = BloomFilter(size=10, number_of_hash_functions=1)
for s in input_strings:
    bloom_filter1.add_string(s=s)

print(bloom_filter1)
print(bloom_filter1.check_membership("gila"))  # this produces a false positive

optimal_filter_size = get_optim_bloom_filter_size(len(input_strings), desired_false_positive_rate=0.001)

optimal_num_of_hash_functions = get_optim_num_of_hash_functs(optimal_filter_size, len(input_strings))

print("optimal filter size would be:", optimal_filter_size)
print("optimal number of hash functions:", optimal_num_of_hash_functions)

bloom_filter2 = BloomFilter(size=optimal_filter_size, number_of_hash_functions=optimal_num_of_hash_functions)
for s in input_strings:
    bloom_filter2.add_string(s=s)

print(bloom_filter2)
print(bloom_filter2.check_membership("gila"))  # this correctly produces a False

