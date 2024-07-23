"""
https://leetcode.com/problems/trapping-rain-water/description/

42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""


def trap(height: list[int]) -> int:
    n = len(height)
    if n <= 2:
        return 0
    lo, hi = 0, n - 1
    left_height = height[0]
    right_height = height[n - 1]
    area = 0
    while lo < hi:
        if left_height < right_height:
            lo += 1
            left_height = max(left_height, height[lo])
            area += left_height - height[lo]
        else:
            hi -= 1
            right_height = max(right_height, height[hi])
            area += right_height - height[hi]
    return area


if __name__ == "__main__":
    height = [4, 2, 0, 3, 2, 5]
    print(trap(height))
