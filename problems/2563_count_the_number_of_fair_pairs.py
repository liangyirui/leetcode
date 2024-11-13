"""
https://leetcode.com/problems/count-the-number-of-fair-pairs/description/

Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper
"""

def countFairPairs(nums: ;ist[int], lower: int, upper: int) -> int:
    nums.sort()
    return self.find(nums, upper + 1) - self.find(nums, lower)

def find(nums: list[int], value: int) -> int:
    lo = 0
    hi = len(nums) - 1
    result = 0
    while lo < hi:
        pair_sum = nums[lo] + nums[hi]
        if pair_sum < value:
            result += hi - lo
            lo += 1
        else:
            hi -= 1
    return result
