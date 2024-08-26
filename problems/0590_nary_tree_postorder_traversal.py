"""
https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/

590. N-ary Tree Postorder Traversal

Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value.
"""

from typing import Self


class Node:
    def __init__(
        self, val: int | None = None, children: list[Self] | None = None
    ) -> None:
        self.val = val
        self.children = children


def postorder(root: Node | None) -> list[int]:
    vals = []

    def dfs(node):
        if node is None:
            return
        for child in node.children:
            dfs(child)
        vals.append(node.val)

    dfs(root)
    return vals


def postorder_iterative(root: Node | None) -> list[int]:
    vals = []
    if root is None:
        return vals
    stack = [root]
    while stack:
        node = stack.pop()
        vals.append(node.val)
        stack.extend(node.children)
    return vals[::-1]
