"""
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/

1493. Longest Subarray of 1's after Deleting One Element

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
"""


def longest_subarray(nums: list[int]) -> int:
    lo = 0
    count = 0
    for hi, num in enumerate(nums):
        count += 1 if num == 0 else 0
        if count > 1:
            count -= 1 if nums[lo] == 0 else 0
            lo += 1
    return hi - lo


if __name__ == "__main__":
    nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
    print(longest_subarray(nums))
