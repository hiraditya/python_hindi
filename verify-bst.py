# Verify if the tree is binary search tree or not

import math
def verify_tree(n, min, max):
    if (n == None):
        return True
    if (n.val < min or n.val > max):
        return False
    # on the left side of a node n.val is the maximum element
    # on the right side of a node n.val is the minimum element
    return verify_tree(n.left, min, n.val) and verify_tree(n.right, n.val, max)

# returns True if the tree is a binary search tree otherwise False.
def verify(r):
    return verify_tree(r, -math.inf, math.inf)