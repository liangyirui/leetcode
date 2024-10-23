"""
https://leetcode.com/problems/cousins-in-binary-tree-ii/description/

Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Return the root of the modified tree.

Note that the depth of a node is the number of edges in the path from the root node to it.
"""

from collections import deque

from _classes import TreeNode

def replace_value_in_tree(root: TreeNode | None) -> TreeNode | None:
    if root is None:
        return root
    level_sums = []
    bfs(root, level_sums)
    queue = deque([root])
    level_idx = 1
    root.val = 0
    while queue:
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()
            sibling_sum = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
            if node.left:
                node.left.val = level_sums[level_idx] - sibling_sum
            	queue.append(node.left)
            if node.right:
                node.right.val = level_sums[level_idx] - sibling_sum
                queue.append(node.right)
        level_idx += 1
    return root
    
def bfs(root: TreeNode | None, vals: list[int]) -> None:
    if root is None:
        return
    queue = deque([root])
    while queue:
        size = len(queue)
        curr_sum = 0
        for _ in range(size):
            node = queue.popleft()
            curr_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        vals.append(curr_sum)