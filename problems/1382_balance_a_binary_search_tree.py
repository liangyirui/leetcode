"""
https://leetcode.com/problems/balance-a-binary-search-tree/description/

1382. Balance a Binary Search Tree

Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.
A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.
"""

from _classes import TreeNode


def balance_BST(root: TreeNode | None) -> TreeNode | None:
    node_vals = []
    inorder(root, node_vals)
    return build_BST(node_vals, 0, len(node_vals) - 1)


def inorder(root: TreeNode | None, node_vals: list[int]) -> None:
    if root is None:
        return
    inorder(root.left, node_vals)
    node_vals.append(root.val)
    inorder(root.right, node_vals)


def build_BST(node_vals: list[int], lo: int, hi: int) -> TreeNode | None:
    if lo > hi:
        return None
    mid = (lo + hi) // 2
    root = TreeNode(node_vals[mid])
    root.left = build_BST(node_vals, lo, mid - 1)
    root.right = build_BST(node_vals, mid + 1, hi)
