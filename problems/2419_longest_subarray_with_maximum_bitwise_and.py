"""
https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description/

You are given an integer array nums of size n.

Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
Return the length of the longest such subarray.

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A subarray is a contiguous sequence of elements within an array.
"""

def longest_subarray(nums: list[int]) -> int:
    max_val = curr = longest = 0
    for num in nums:
        if max_val < num:
            max_val = num
            longest = curr = 0
        if max_val == num:
            curr += 1
        else:
            curr = 0
        longest = max(longest, curr)
    return longest