"""
https://leetcode.com/problems/maximum-xor-for-each-query/description/

You are given a sorted array nums of n non-negative integers and an integer maximumBit. You want to perform the following query n times:

1. Find a non-negative integer k < 2maximumBit such that nums[0] XOR nums[1] XOR ... XOR nums[nums.length-1] XOR k is maximized. k is the answer to the ith query.
2. Remove the last element from the current array nums.

Return an array answer, where answer[i] is the answer to the ith query.
"""

def get_maximum_xor(nums: list[int], maximum_bit: int) -> list[int]:
    n = len(nums)
    xor = 0
    answer = [0] * n
    for num in nums:
        xor ^= num
    mask = (1 << maximum_bit) - 1
    for i in range(n):
        answer[i] = xor ^ mask
        xor ^= nums[n - 1 - i]
    return answer
