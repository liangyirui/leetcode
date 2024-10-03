"""
https://leetcode.com/problems/make-sum-divisible-by-p/description/

Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.
"""

def min_subarray(nums: list[int], p: int) -> int:
    n = len(nums)
    target = sum(nums) % p
    if target == 0:
        return 0
    mod_map = {0: -1}
    curr = 0
    min_len = n
    for i, num in enumerate(nums):
        curr = (curr + num) % p
        mod_map[curr] = i
        need = (curr - target + p) % p
        if need in mod_map:
            min_len = min(min_len, i - mod_map[need])
    return min_len if min_len < n else -1