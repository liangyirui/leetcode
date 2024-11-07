"""
https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/description/

The bitwise AND of an array nums is the bitwise AND of all integers in nums.

For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1.
Also, for nums = [7], the bitwise AND is 7.

You are given an array of positive integers candidates. Evaluate the bitwise AND of every combination of numbers of candidates. Each number in candidates may only be used once in each combination.
Return the size of the largest combination of candidates with a bitwise AND greater than 0.

Constraints:
1 <= candidates.length <= 10^5
1 <= candidates[i] <= 10^7
"""


def largest_combination(self, candidates: list[int]) -> int:
    largest = 0
    for i in range(24):
        count = 0
        for num in candidates:
            count += (num >> i) & 1
        largest = max(largest, count)
    return largest
