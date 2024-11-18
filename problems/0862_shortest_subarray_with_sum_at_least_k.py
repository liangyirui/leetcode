"""
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/

Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.
"""

import heapq
from collections import deque


def shortest_subarray(nums: list[int], k: int) -> int:
    n = len(nums)
    prefix_sum = [0]
    for num in nums:
        prefix_sum.append(prefix_sum[-1] + num)
    monoq = deque()
    ans = n + 1
    for i, num in enumerate(prefix_sum):
        while monoq and num <= prefix_sum[monoq[-1]]:
            monoq.pop()
        while monoq and num - prefix_sum[monoq[0]] >= k:
            ans = min(ans, i - monoq.popleft())
        monoq.append(i)
    return ans if ans < n + 1 else -1


def shortest_subarray_pq(nums: list[int], k: int) -> int:
    n = len(nums)
    ans = n + 1
    pq = []
    curr_sum = 0
    for i, num in enumerate(nums):
        curr_sum += num
        if curr_sum >= k:
            ans = min(ans, i + 1)
        while pq and curr_sum - pq[0][0] >= k:
            ans = min(ans, i - heapq.heappop(pq)[1])
        heapq.heappush(pq, (curr_sum, i))
    return ans if ans < n + 1 else -1


if __name__ == "__main__":
    nums = [2, -1, 2]
    k = 3
    print(shortest_subarray(nums, k))
    print(shortest_subarray_pq(nums, k))
