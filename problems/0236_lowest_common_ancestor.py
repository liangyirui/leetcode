"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

236. Lowest Common Ancestor of a Binary Tree
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
"""

from _classes import TreeNode


def lowest_common_ancestor(
    root: TreeNode | None, p: TreeNode, q: TreeNode
) -> TreeNode | None:
    path_p = []
    path_q = []
    find_path(root, p.val, path_p)
    find_path(root, q.val, path_q)
    i = 0
    while i < len(path_p) and i < len(path_q):
        if path_p[i] != path_q[i]:
            break
        i += 1
    return path_p[i - 1]


def find_path(root: TreeNode | None, target: int, path: list[TreeNode]) -> bool:
    if root is None:
        return False
    path.append(root)
    if root.val == target:
        return True
    if (root.left and find_path(root.left, target, path)) or (
        root.right and find_path(root.right, target, path)
    ):
        return True
    path.pop()
    return False


def lca(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
    if root is None or p is root or q is root:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left is None:
        return right
    if right is None:
        return left
    return root
