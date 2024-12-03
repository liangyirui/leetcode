"""
https://leetcode.com/problems/max-consecutive-ones-iii/description/


1004. Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
"""


def longest_ones(nums: list[int], k: int) -> int:
    # sliding window without shrinking
    lo = 0
    for hi, num in enumerate(nums):
        k -= 1 if num == 0 else 0
        if k < 0:
            k += 1 if nums[lo] == 0 else 0
            lo += 1
    return hi - lo + 1


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k = 3
    print(longest_ones(nums, k))
