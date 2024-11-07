"""
https://leetcode.com/problems/maximal-score-after-applying-k-operations/description/

You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.

In one operation:

1. choose an index i such that 0 <= i < nums.length,
2. increase your score by nums[i], and
3. replace nums[i] with ceil(nums[i] / 3).
Return the maximum possible score you can attain after applying exactly k operations.
The ceiling function ceil(val) is the least integer greater than or equal to val.
"""

import heapq

def max_k_elements(nums: list[int], k: int) -> int:
    pq = []
    for num in nums:
        heapq.heappush(pq, -num)
    score = 0
    for _ in range(k):
        num = -heapq.heappop(pq)
        score += num
        heapq.heappush(pq, -num // 3)
    return score
