"""
https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/description/

1508. Range Sum of Sorted Subarray Sums

You are given the array nums consisting of n positive integers. You computed the sum of all non-empty continuous subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.
Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the answer can be a huge number return it modulo 10^9 + 7.
"""

import heapq


def range_sum(nums: list[int], left: int, right: int) -> int:
    n = len(nums)
    pq = []
    for i, num in enumerate(nums):
        heapq.heappush(pq, (num, i))

    ans = 0
    mod = 10**9 + 7
    for i in range(1, right + 1):
        num, j = heapq.heappop(pq)
        if i >= left:
            ans = (ans + num) % mod
        if j < n - 1:
            heapq.heappush(pq, (num + nums[j + 1], j + 1))
    return ans


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    left = 1
    right = 10
    print(range_sum(nums, left, right))
