"""
https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/

Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
"""


def count_pairs(nums: list[int], target: int) -> int:
    nums.sort()
    n = len(nums)
    lo, hi = 0, n - 1
    count = 0
    while lo < hi:
        if nums[lo] + nums[hi] < target:
            count += hi - lo
            lo += 1
        else:
            hi -= 1
    return count


if __name__ == "__main__":
    nums = [-1, 1, 2, 3, 1]
    target = 2
    print(count_pairs(nums, target))
