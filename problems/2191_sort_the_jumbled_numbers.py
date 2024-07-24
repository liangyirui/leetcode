"""
https://leetcode.com/problems/sort-the-jumbled-numbers/description/

2191. Sort the Jumbled Numbers

You are given a 0-indexed integer array mapping which represents the mapping rule of a shuffled decimal system. mapping[i] = j means digit i should be mapped to digit j in this system.

The mapped value of an integer is the new integer obtained by replacing each occurrence of digit i in the integer with mapping[i] for all 0 <= i <= 9.

You are also given another integer array nums. Return the array nums sorted in non-decreasing order based on the mapped values of its elements.

Notes:

Elements with the same mapped values should appear in the same relative order as in the input.
The elements of nums should only be sorted based on their mapped values and not be replaced by them.
"""


def sort_jumbled(mapping: list[int], nums: list[int]) -> list[int]:
    pairs = []
    for i, num in enumerate(nums):
        mapped_num = 0
        place = 1
        if num == 0:
            pairs.append((mapping[0], i))
            continue
        while num > 0:
            mapped_num += mapping[num % 10] * place
            num //= 10
            place *= 10
        pairs.append((mapped_num, i))

    pairs.sort()
    return [nums[i] for num, i in pairs]


if __name__ == "__main__":
    mapping = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6]
    nums = [991, 338, 38]
    print(sort_jumbled(mapping, nums))
