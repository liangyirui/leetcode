"""
https://leetcode.com/problems/sort-colors/description/

75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
"""


def sort_colors(nums: list[int]) -> None:
    n = len(nums)
    lo, hi = 0, n - 1
    i = 0
    while i <= hi:
        if nums[i] == 0:
            nums[lo], nums[i] = nums[i], nums[lo]
            lo += 1
            i += 1
        elif nums[i] == 2:
            nums[hi], nums[i] = nums[i], nums[hi]
            hi -= 1
        else:
            i += 1


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    print(nums)
    sort_colors(nums)
    print(nums)
