"""
https://leetcode.com/problems/delete-nodes-and-return-forest/description/

1110. Delete Nodes and Return Forest

Given the root of a binary tree, each node in the tree has a distinct value.
After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
Return the roots of the trees in the remaining forest. You may return the result in any order.
"""

from collections import deque

from problems._classes import TreeNode


def del_nodes(root: TreeNode | None, to_delete: list[int]) -> list[TreeNode]:
    delete_set = set(to_delete)
    forest = []
    root = dfs(root, delete_set, forest)
    if root is not None:
        forest.append(root)
    return forest


def dfs(
    node: TreeNode | None, delete_set: set, forest: list[TreeNode]
) -> TreeNode | None:
    if node is None:
        return None
    node.left = dfs(node.left, delete_set, forest)
    node.right = dfs(node.right, delete_set, forest)
    if node.val in delete_set:
        if node.left:
            forest.append(node.left)
        if node.right:
            forest.append(node.right)
        return None
    return node


def bfs(root: TreeNode | None, to_delete: list[int]) -> list[TreeNode]:
    forest = []
    if root is None:
        return forest
    delete_set = set(to_delete)
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
            if node.left.val in delete_set:
                node.left = None
        if node.right:
            queue.append(node.right)
            if node.right.val in delete_set:
                node.right = None
        if node.val in delete_set:
            if node.left:
                forest.append(node.left)
            if node.right:
                forest.append(node.right)

    if root.val not in to_delete:
        forest.append(root)

    return forest
