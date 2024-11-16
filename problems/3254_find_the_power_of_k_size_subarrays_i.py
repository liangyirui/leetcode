"""
https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/description/

You are given an array of integers num of length n and a positive integer k.

The power of an array is defined as

1. Its maximum element if all of its elements are consecutive and sorted in ascending order.
2. -1 otherwise.

You need to find the power of all subarrays of nums of size k.
Return an integer array results of size n - k + 1, where results[i] is the power of nums[i...(i - k - 1)].
"""


def results_array(nums: list[int], k: int) -> list[int]:
    if k == 1:
        return nums
    n = len(nums)
    results = [-1] * (n - k + 1)
    count = 1
    for i in range(n - 1):
        if nums[i] + 1 == nums[i + 1]:
            count += 1
        else:
            count = 1
        if count >= k:
            results[i - k + 2] = nums[i + 1]
    return results
