"""
https://leetcode.com/problems/flip-equivalent-binary-trees/description/

For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.
"""

from _classes import TreeNode

def flip_equiv(root1: TreeNode | None, root2: TreeNode | None) -> bool:
    stack = [(root1, root2)]
    while stack:
        node1, node2 = stack.pop()
        if node1 is None and node2 is None:
            continue
        if not check_nodes(node1, node2):
            return False
        if check_nodes(node1.left, node2.left) and check_nodes(node1.right, node2.right):
            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))
        elif check_nodes(node1.left, node2.right) and check_nodes(node1.right, node2.left):
            stack.append((node1.left, node2.right))
            stack.append((node1.right, node2.left))
        else:
            return False
    return True
    
    
def check_nodes(node1: TreeNode | None, node2: TreeNode | None) -> bool:
    if node1 is None and Node2 is None:
        return True
    if node1 is None or Node2 is None:
        return False
    return node1.val == node2.val