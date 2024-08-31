"""
https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/description/

2096. Step-by-step Directions from a Binary Tree Node to Another

You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.
Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:
'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.
"""

from _classes import TreeNode


def get_directions(root: TreeNode | None, start_value: int, dest_value: int) -> str:
    root_to_start = []
    root_to_dest = []
    find_path(root, start_value, root_to_start)
    find_path(root, dest_value, root_to_dest)
    i = 0
    while i < len(root_to_start) and i < len(root_to_dest):
        if root_to_start[i] == root_to_dest[i]:
            break
        i += 1
    directions = ["U"] * (len(root_to_start) - i)
    directions.extend(root_to_dest[i:])
    return "".join(directions)


def find_path(root: TreeNode | None, target: int, path: list[str]) -> bool:
    if root is None:
        return False
    if root.val == target:
        return True
    # Try left subtree
    path.append("L")
    if find_path(root.left, target, path):
        return True
    path.pop()
    # Try right subtree
    path.append("R")
    if find_path(root.right, target, path):
        return True
    path.pop()
    # Not found
    return False
