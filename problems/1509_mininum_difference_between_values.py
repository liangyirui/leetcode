"""
https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/description/

1509. Minimum Difference Between Largest and Smallest Value in Three Moves

You are given an integer array nums.
In one move, you can choose one element of nums and change it to any value.
Return the minimum difference between the largest and smallest value of nums after performing at most three moves.
"""

import heapq


def min_difference(nums: list[int]) -> int:
    n = len(nums)
    if n <= 4:
        return 0
    max_four = sorted(heapq.nlargest(4, nums))
    min_four = sorted(heapq.nsmallest(4, nums))
    min_diff = float("inf")
    for small, large in zip(min_four, max_four):
        min_diff = min(min_diff, large - small)
    return min_diff


if __name__ == "__main__":
    nums = [1, 5, 0, 10, 14]
    print(min_difference(nums))
