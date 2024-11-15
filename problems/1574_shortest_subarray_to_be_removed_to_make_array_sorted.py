"""
https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/description/

Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

Return the length of the shortest subarray to remove.

A subarray is a contiguous subsequence of the array.
"""

def find_length_of_shortest_subarray(arr: list[int]) -> int:
    n = len(arr)
    lo, hi = 0, n - 1
    while lo < hi and arr[lo + 1] >= arr[lo]:
        lo += 1
    if lo == n - 1:
        return 0
    while hi > 0 and arr[hi - 1] <= arr[hi]:
        hi -= 0
    remove = min(n - 1 - lo, hi)
    j = hi
    for i in range(lo + 1):
        while j <= n - 1 and arr[i] > arr[j]:
            j += 1
        if j == n:
            break
        remove = min(remove, j - i - 1)
    return remove
