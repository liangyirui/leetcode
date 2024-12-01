"""
https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description/

632. Smallest Range Covering Elements from K Lists

You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.
We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.
"""

import heapq


def smallest_range(nums: list[list[int]]) -> list[int]:
    k = len(nums)
    pq = []
    max_val = float("-inf")
    start, end = 0, float("inf")
    for i in range(k):
        heapq.heappush(pq, (nums[i][0], i, 0))
        max_val = max(max_val, nums[i][0])

    while len(pq) == k:
        min_val, row, col = heapq.heappop(pq)
        if max_val - min_val < end - start:
            start, end = min_val, max_val

        if col + 1 < len(nums[row]):
            next_val = nums[row][col + 1]
            heapq.heappush(pq, (next_val, row, col + 1))
            max_val = max(max_val, next_val)

    return [start, end]


if __name__ == "__main__":
    nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    print(smallest_range(nums))
