"""
https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/

You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.

Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.
"""

from collections import defaultdict


def maximum_subarray_sum(nums: list[int], k: int) -> int:
    count = defaultdict(int)
    lo = 0
    max_sum = curr_sum = 0
    for hi, num in enumerate(nums):
        curr_sum += num
        count[num] += 1
        if hi - lo + 1 > k:
            count[nums[lo]] -= 1
            curr_sum -= nums[lo]
            if count[nums[lo]] == 0:
                del count[nums[lo]]
            lo += 1
        if len(count) == k:
            max_sum = max(max_sum, curr_sum)
    return max_sum


if __name__ == "__main__":
    nums = [1, 5, 4, 2, 9, 9, 9]
    k = 3
    print(maximum_subarray_sum(nums, k))
