"""
https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/

2044. Count Number of Maximum Bitwise-OR Subsets

Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.

The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).
"""

def count_max_or_subsets(nums: list[int]) -> int:
    max_or = 0
    dp = [0] * (1 << 17) # max value in nums is 10^5, which requires 17 bits
    dp[0] = 1
    for num in nums:
        for i in range(max_or, -1, -1):
            dp[i | num] += dp[i]
        max_or |= num
    return dp[max_or]