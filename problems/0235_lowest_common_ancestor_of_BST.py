"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

235. Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""

from classes import TreeNode


def lca_recursive(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
    lo, hi = min(p.val, q.val), max(p.val, q.val)
    if root.val < lo:
        return lca_recursive(root.right, p, q)
    if root.val > hi:
        return lca_recursive(root.right, p, q)
    return root


def lca_iterative(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
    lo, hi = min(p.val, q.val), max(p.val, q.val)
    node = root
    while node:
        if node.val < lo:
            node = node.right
        elif node.val > hi:
            node = node.left
        else:
            return node
    return None
