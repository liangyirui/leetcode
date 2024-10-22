"""
https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description/

You are given the root of a binary tree and a positive integer k.

The level sum in the tree is the sum of the values of the nodes that are on the same level.

Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.

Note that two nodes are on the same level if they have the same distance from the root.
"""

from collections import deque

from _classes import TreeNode

def kth_largest_level_sum(root: TreeNode | None, k: int) -> int:
    level_sum = []
    bfs(root, level_sum)
    n = len(level_sum)
    if k > n:
        return -1
    k = n - k
    return quickselect(level_sum, k)
    
    
def bfs(root: TreeNode | None, vals: list[int]) -> None:
    q = deque([root])
    while q:
        size = len(q)
        curr_sum = 0
        for _ in range(size):
            node = q.popleft()
            curr_sum += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        vals.append(curr_sum)
        

def quickselect(arr: list[int], k: int) -> int:
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = partition(lo, hi)
        if mid < k:
            lo = mid + 1
        elif pivot > k:
            hi = mid - 1
        else:
            break
    return arr[k]
    
    
def partition(arr: list[int], lo: int, hi: int) -> int:
    pivot = lo
    while True:
        if arr[lo] < arr[pivot]:
            lo += 1
        elif arr[hi] > arr[pivot]:
            hi -= 1
        elif lo < hi:
            arr[lo], arr[hi] = arr[hi], arr[lo]
            lo += 1
            hi -= 1
        else:
            arr[pivot], arr[hi] = arr[hi], arr[pivot]
            break
    return hi