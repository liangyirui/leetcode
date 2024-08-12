"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:
KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
"""

import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]) -> None:
        self.pq = []
        self.k = k
        for num in nums:
            heapq.heappush(self.pq, num)
            if len(self.pq) > k:
                heapq.heappop(self.pq)

    def add(self, val: int) -> int:
        heapq.heappush(self.pq)
        if len(self.pq) > self.k:
            heapq.heappop(self.pq)
        return self.pq[0]
