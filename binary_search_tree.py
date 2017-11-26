# How to implement binary search tree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None # left-edge
        self.right = None # right-edge


class binary_tree:
    def __init__(self):
        self.root = None

    # Add node
    def add(self, val):
        if (self.root == None):
            self.root = Node(val)
        else:
            self.add_node(self.root, val)

    # node should not be None
    # mutually recursive functions by factoring out functionalities
    def add_node(self, node, val):
        if (node.val < val):
            self.add_right(node, val)
        else: # node.val >= val
            self.add_left(node, val)

    def add_right(self, node, val):
        if (node.right == None):
            node.right = Node(val)
        else:
            self.add_node(node.right, val)

    def add_left(self, node, val):
        if (node.left == None):
            node.left = Node(val)
        else:
            self.add_node(node.left, val)

    # Search for a value. Setup the recursion
    def find(self, val):
        if (self.root == None):
            return None
        else:
            return self.find_node(self.root, val)

    # Recursively find the value in the binary search tree with \p node as root.
    def find_node(self, node, val):
        if (node == None):
            return None
        if (node.val == val):
            return node
        if (node.val < val):
            #print(node.val, "less than", val, "going right")
            return self.find_node(node.right, val)
        else:
            #print(node.val, "greater than", val, "going left")
            return self.find_node(node.left, val)

    # Utilities to print the binary tree
    def print_tree(self):
        if(self.root != None):
            print('digraph structs {\nnode [shape=record];')
            self._print_label(self.root)
            self._print_tree(self.root)
            print('}')

    def _print_label(self, node):
        if(node != None):
            # struct1 [label="<f0>|0|<f1>"];
            print('struct' + str(node.val) + '[label="<f0>|' + str(node.val) + '|<f1>"];')
            self._print_label(node.left)
            self._print_label(node.right)

    def _print_tree(self, node):
        if(node != None):
            # struct1:f1 -> struct2;
            if (node.left != None):
                print('struct' + str(node.val) + ':f0 -> struct' + str(node.left.val))
            if (node.right != None):
                print('struct' + str(node.val) + ':f1 -> struct' + str(node.right.val))
            self._print_tree(node.left)
            self._print_tree(node.right)


tree = binary_tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(8)
tree.add(2)

# Search for values in a binary search tree.
'''
n1 = tree.find(0)
if (n1 != None):
    print("Found ", n1.val)
else:
    print("0 Not found")

n2 = tree.find(10)
if (n2 != None):
    print("Found ", n2.val)
else:
    print("10 Not found")
'''


import math
# Verify if the tree is binary or not

def verify_for_range(t, min, max):
    if t == None:
        return True
    if t.val <= min or t.val > max:
        return False
    return verify_for_range(t.left, min, t.val) and verify_for_range(t.right, t.val, max)


def verify(t):
    return verify_for_range(t, -math.inf, math.inf)


print(verify(tree.root))

# graphviz: paste the output in graph.dot
# use dot -Tpdf graph.dot -o graph.pdf
#tree.print_tree()
