"""
https://leetcode.com/problems/rank-transform-of-an-array/description/

1331. Rank Transform of an Array

Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
"""

def array_rank_transform(arr: list[int]) -> list[int]:
    sorted_arr = sorted(arr)
    rank_map = {}
    rank = 0
    for num in sorted_arr:
        if num not in rank_map:
            rank += 1
        rank_map[num] = rank
    array_rank = []
    for num in arr:
        array_rank.append(rank_map[num])
    return array_rank