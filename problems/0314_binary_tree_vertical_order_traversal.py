"""
https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/

314. Binary Tree Vertical Order Traversal

Given the root of a binary tree, return the vertical order traversal of its nodes' values (i.e., from top to bottom, column by column).
If two nodes are in the same row and column, the order should be from left to right.
"""

from collections import defaultdict, deque

from problems._classes import TreeNode


def vertical_order(root: TreeNode | None) -> list[list[int]]:
    if root is None:
        return []
    queue = deque([(root, 0)])
    col_node = defaultdict(list)
    min_col = max_col = 0
    while queue:
        node, col = queue.popleft()
        col_node[col].append(node.val)
        min_col = min(min_col, col)
        max_col = max(max_col, col)
        if node.left:
            queue.append((node.left, col - 1))
        if node.right:
            queue.append((node.right, col + 1))
    return [col_node[i] for i in range(min_col, max_col + 1)]


def vertical_order_dfs(root: TreeNode | None) -> list[list[int]]:
    if root is None:
        return []
    col_nodes = defaultdict(list)
    min_col = max_col = 0

    def dfs(node, row, col):
        nonlocal min_col, max_col
        if node is None:
            return
        col_nodes[col].append((row, node.val))
        min_col = min(min_col, col)
        max_col = max(max_col, col)
        dfs(node.left, row + 1, col - 1)
        dfs(node.right, row + 1, col + 1)

    dfs(root, 0, 0)
    order = []
    for col in range(min_col, max_col + 1):
        col_nodes[col].sort(key=lambda x: x[0])
        col_vals = [val for row, val in col_nodes[col]]
        order.append(col_vals)
    return order
