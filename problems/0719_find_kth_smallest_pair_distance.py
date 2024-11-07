"""
https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/

719. Find K-th Smallest Pair Distance

The distance of a pair of integers a and b is defined as the absolute difference between a and b.
Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.
"""


def smallest_distance_pair(nums: list[int], k: int) -> int:
    nums.sort()
    n = len(nums)
    lo, hi = 0, nums[n - 1] - nums[0]
    while lo < hi:
        mid = (lo + hi) // 2
        count = 0
        j = 0
        for i in range(n):
            while j < n and nums[j] <= nums[i] + mid:
                j += 1
            count += j - i - 1
        if count < k:
            lo = mid + 1
        else:
            hi = mid
    return lo


if __name__ == "__main__":
    nums = [1, 6, 1]
    k = 3
    print(smallest_distance_pair(nums, k))
