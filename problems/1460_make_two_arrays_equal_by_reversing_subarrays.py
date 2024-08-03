"""
https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/description/

1460. Make Two Arrays Equal by Reversing Subarrays

You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray of arr and reverse it. You are allowed to make any number of steps.
Return true if you can make arr equal to target or false otherwise.
"""


def can_be_equal(target: list[int], arr: list[int]) -> bool:
    freq: list[int] = [0] * 1001
    for num1, num2 in zip(target, arr):
        freq[num1] += 1
        freq[num2] -= 1
    return all([item == 0 for item in freq])


if __name__ == "__main__":
    target = [1, 2, 3, 4]
    arr = [2, 4, 1, 3]
    print(can_be_equal(target, arr))
