"""
https://leetcode.com/problems/largest-number/description/

179. Largest Number

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be large, you need to return a string instead of an integer.
"""

from functools import cmp_to_key

def largest_number(nums: list[int]) -> str:
    num_strings = [str(num) for num in nums]
    num_strings.sort(key = cmp_to_key(cmp_func), reverse = True)
    if num_strings[0] == "0":
        return "0"
    return "".join(num_strings)
    
def cmp_func(a: str, b: str) -> int:
    if a + b > b + a:
        return 1
    if a == b:
        return 0
    return -1: