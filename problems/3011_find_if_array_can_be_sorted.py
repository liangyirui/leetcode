"""
https://leetcode.com/problems/find-if-array-can-be-sorted/description/

You are given a 0-indexed array of positive integers nums.

In one operation, you can swap any two adjacent elements if they have the same number of
set bits. You are allowed to do this operation any number of times (including zero).

Return true if you can sort the array, else return false.
"""


def can_sort_array(nums: list[int]) -> bool:
    n = len(nums)
    prev_max = float("-inf")
    curr_min = curr_max = nums[0]
    count = bin(nums[0]).count("1")
    for i in range(1, n):
        if bin(nums[i]).count("1") == count:
            curr_min = min(curr_min, nums[i])
            curr_max = max(curr_max, nums[i])
        else:
            if curr_min < prev_max:
                return False
            prev_max = curr_max
            curr_min = curr_max = nums[i]
            count = bin(nums[i]).count("1")
    # Final check
    if curr_min < prev_max:
        return False
    return True


if __name__ == "__main__":
    nums = [8, 4, 2, 30, 15]
    print(can_sort_array(nums))
