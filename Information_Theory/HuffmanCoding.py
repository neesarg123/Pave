import math 


class BinaryTreeNode:
    def __init__(self, value, id=None, prime=0):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.bit = "" 
        self.id = id 
        self.prime = prime
        
    def __str__(self):
        return "(Value: " + str(self.value) + "\nBit: " + str(self.bit) + " id: " + str(self.id) + " prime: " + \
                str(self.prime) + "\nL.C.: " + str(self.left_child) + "\nR.C.: " + str(self.right_child) + ")"


def has_path(root, arr, x):
    # if root is None there is no path
    if (not root):
        return False
     
    # push the node's value in 'arr'
    arr.append(root.bit)    
     
    # if it is the required node
    # return true
    if (root.id == x and root.prime == 0):    
        return True
     
    # else check whether the required node
    # lies in the left subtree or right
    # subtree of the current node
    if (has_path(root.left_child, arr, x) or
        has_path(root.right_child, arr, x)):
        return True
     
    # required node does not lie either in
    # the left or right subtree of the current
    # node. Thus, remove current node's value 
    # from 'arr' and then return false    
    arr.pop(-1)

    return False


# function to print the path from root to
# the given node if the node lies in
# the binary tree
def print_path(root, x):
     
    # vector to store the path
    arr = []
     
    # if required node 'x' is present
    # then print the path
    if (has_path(root, arr, x)):
        for i in range(len(arr) - 1):
            print(arr[i], end = "")
        print(arr[len(arr) - 1])
     
    # 'x' is not present in the
    # binary tree
    else:
        print("No Path")
    
    return arr


# calculate average entropy (bits/symbol) H(x) = summation of products of P(x) * log_2(1/P(x))
def H(probabilities):
    return sum([p * math.log(1/p,2) for p in probabilities])


# calculate average code length K = P(x) * Code Length
def K(probabilities, code_lengths):
    return sum([p * cl for (p, cl) in zip(probabilities, code_lengths)])    


# calculate code efficiency: H(x) / K 
def efficiency(H, K):
    return H / K


# sample inputs (probabilities)
symb_num = int(input("How many symbols need to be encoded? "))
X = []
for j in range(symb_num):
    prob_value = float(input("Enter Probability for X" + str(j + 1) + ": "))
    X.append(BinaryTreeNode(value=prob_value, id=j+1))

# iterator i for id 
i = len(X) + 1
# save copy of X's length
X_len = len(X)
# save a copy of X for later use 
X_copy = X.copy()

while len(X) >= 2: 
    # ensure X is sorted (descending order)
    X.sort(key=lambda x: (x.value, x.prime), reverse=True)

    # for x in X:
    #     print(x)
    # print()

    # replace last two nodes with another node: Xn
    # Xn will have value of X[-1] + X[-2] 
    # Xn will be parent of X[-1] and X[-2] 
    Xn = BinaryTreeNode(X[-1].value + X[-2].value, id=X[-2].id, prime=1)
    Xn.left_child = X[-1]
    Xn.left_child.bit = "1" 
    Xn.right_child = X[-2]
    Xn.right_child.bit = "0"
    
    X[-2:] = [Xn]
    i += 1

code_lengths = [] 

for j in range(X_len):
    print("X" + str(j + 1) + ":", end=" ")
    code_lengths.append(len(print_path(X[0], j + 1)) - 1)  # also prints the path 

# print(X[0])
H = H([x.value for x in X_copy])
K = K([x.value for x in X_copy], code_lengths)
print("H(X) in bits/symbol:", str(H))
print("K in number of bits:", str(K))
print("Code Efficiency:", str(efficiency(H, K)))

