"""
https://leetcode.com/problems/sort-array-by-increasing-frequency/description/

1636. Sort Array by Increasing Frequency

Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.
Return the sorted array.
"""

from collections import Counter


def frequency_sort(nums: list[int]) -> list[int]:
    freq = Counter(nums)
    return sorted(nums, key=lambda x: (freq[x], -x))


if __name__ == "__main__":
    nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
    print(frequency_sort(nums))
