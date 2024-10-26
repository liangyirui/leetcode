"""
https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/description/

You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n. You are also given an array queries of size m.

You have to perform m independent queries on the tree where in the ith query you do the following:

Remove the subtree rooted at the node with the value queries[i] from the tree. It is guaranteed that queries[i] will not be equal to the value of the root.
Return an array answer of size m where answer[i] is the height of the tree after performing the ith query.

Note:

The queries are independent, so the tree returns to its initial state after each query.
The height of a tree is the number of edges in the longest simple path from the root to some node in the tree.
"""

from collections import defaultdict

from _classes import TreeNode

def tree_queries(root: TreeNode | None, queries: list[int]) -> list[int]:
    depth, height = defaultdict(int), defaultdict(int)
    
    def dfs(node, d):
        if node is None:
            return -1
        depth[node.val] = d
        curr = max(dfs(node.left, d + 1), dfs(node.right, d + 1)) + 1
        height[node.val] = curr
        return curr
        
    dfs(root, 0)
    
    cousins = defaultdict(list)
    for val, d in depth.items():
        cousins[d].append((-height[val], val))
        cousins[d].sort()
        if len(cousins[d]) > 2:
            cousins[d].pop()
            
    result = []
    for q in queries:
        d = depth[q]
        if len(cousins[d]) == 1:
            result.append(d - 1)
        elif cousins[d][0][1] == q:
            result.append(-cousins[d][1][0] + d)
        else:
            result.append(-cousins[d][0][0] + d)
    return result