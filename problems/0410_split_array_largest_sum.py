"""
https://leetcode.com/problems/split-array-largest-sum/description/

410. Split Array Largest Sum

Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.
Return the minimized largest sum of the split.
A subarray is a contiguous part of the array.
"""


def split_array(nums: list[int], k: int) -> int:
    lo, hi = max(nums), sum(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if can_split(nums, k, mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


def can_split(nums: list[int], k: int, max_sum_allowed: int) -> bool:
    split = 0
    curr_sum = 0
    for num in nums:
        if curr_sum + num <= max_sum_allowed:
            curr_sum += num
        else:
            curr_sum = num
            split += 1
    return split + 1 <= k


if __name__ == "__main__":
    nums = [7, 2, 5, 10, 8]
    k = 2
    print(split_array(nums, k))
