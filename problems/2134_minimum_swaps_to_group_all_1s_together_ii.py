"""
https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/description/

2134. Minimum Swaps to Group All 1's Together II

A swap is defined as taking two distinct positions in an array and swapping the values in them.
A circular array is defined as an array where we consider the first element and the last element to be adjacent.
Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.
"""


def min_swaps(nums: list[int]) -> int:
    total = sum(nums)
    swaps = total
    n = len(nums)
    left = 0
    curr_sum = 0
    for right in range(n + total):
        curr_sum += nums[right % n]
        if right - left + 1 > total:
            curr_sum -= nums[left]
            left += 1
        if right >= total - 1:
            swaps = min(swaps, total - curr_sum)
    return swaps


if __name__ == "__main__":
    nums = [0, 1, 1, 1, 0, 0, 1, 1, 0]
    print(min_swaps(nums))
