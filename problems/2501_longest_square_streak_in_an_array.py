"""
https://leetcode.com/problems/longest-square-streak-in-an-array/description/

You are given an integer array nums. A subsequence of nums is called a square streak if:

The length of the subsequence is at least 2, and
after sorting the subsequence, each element (except the first element) is the square of the previous number.
Return the length of the longest square streak in nums, or return -1 if there is no square streak.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
"""

def longest_square_streak(nums: list[int]) -> int:
    max_streak = 0
    nums_set = set(nums)
    for num in nums:
        curr_streak = 0
        curr = num
        while curr in nums_set:
            curr_streak += 1
            curr *= curr
        max_streak = max(max_streak, curr_streak)
    return max_streak if max_streak > 1 else -1