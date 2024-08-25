"""
https://leetcode.com/problems/binary-tree-postorder-traversal/description/

145. Binary Tree Postorder Traversal

Given the root of a binary tree, return the postorder traversal of its nodes' values.
"""

from collections import deque

from _classes import TreeNode


def postorder_traversal(root: TreeNode | None) -> list[int]:
    vals = deque()
    stack = []
    if root is None:
        return vals
    stack.append(root)
    while stack:
        curr = stack.pop()
        vals.appendleft(curr.val)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    return vals
