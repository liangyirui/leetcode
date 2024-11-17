"""
https://leetcode.com/problems/minimum-size-subarray-sum/description/

Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""


def min_subarray_len(target: int, nums: list[int]) -> int:
    n = len(nums)
    size = n + 1
    lo = 0
    curr_sum = 0
    for hi, num in enumerate(nums):
        curr_sum += num
        while curr_sum >= target:
            size = min(size, hi - lo + 1)
            curr_sum -= nums[lo]
            lo += 1
    return size % (n + 1)


if __name__ == "__main__":
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(min_subarray_len(target, nums))
