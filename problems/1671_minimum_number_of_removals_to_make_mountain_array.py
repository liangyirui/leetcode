"""
https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/description/

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array nums​​​, return the minimum number of elements to remove to make nums​​​ a mountain array.
"""

def minimum_mountain_removals(nums: list[int]) -> int:
    n = len(nums)
    lis = [1] * n     # longest increasing sequence
    lds = [1] * n     # longest decreasing sequence
    min_removals = n + 1
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                lds[i] = max(lds[i], lds[j] + 1)
    for i in range(n):
        if lis[i] > 1 and lds[i] > 1:
            min_removals = min(min_removals, n - lis[i] - lds[i] + 1)
    return min_removals