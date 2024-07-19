"""
https://leetcode.com/problems/number-of-good-leaf-nodes-pairs

1530. Number of Good Leaf Nodes Pairs

You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.
Return the number of good leaf node pairs in the tree.
"""

from classes import TreeNode


def count_pairs(root: TreeNode, distance: int) -> int:
    count = 0

    def dfs(node: TreeNode | None) -> list[int]:
        nonlocal count
        if node is None:
            return []
        if node.left is None and node.right is None:
            return [1]
        left = dfs(node.left)
        right = dfs(node.right)
        count += sum(l_dist + r_dist <= distance for l_dist in left for r_dist in right)
        return [n + 1 for n in left + right if n <= distance]

    dfs(root)
    return count
