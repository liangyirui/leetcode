"""
https://leetcode.com/problems/maximum-distance-in-arrays/description/

624. Maximum Distance in Arrays

You are given m arrays, where each array is sorted in ascending order.
You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.
Return the maximum distance.
"""


def max_distance(arrays: list[list[int]]) -> int:
    min_val = float("inf")
    max_val = -float("inf")
    ans = 0
    for arr in arrays:
        ans = max(ans, max_val - arr[0], arr[-1] - min_val)
        min_val = min(min_val, arr[0])
        max_val = max(max_val, arr[-1])
    return ans


if __name__ == "__main__":
    arrays = [[1, 2, 3], [4, 5], [1, 2, 3]]
    print(max_distance(arrays))
