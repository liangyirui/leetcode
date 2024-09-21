"""
https://leetcode.com/problems/lexicographical-numbers/description/

Given an integer n, return all numbers in the range [1,n] sorted in lexicographical order.
You must write an algorithm that runs in O(n) time and uses O(1) extra space.
"""

def lexical_order(n: int) -> list[int]:
    curr = 1
    nums = []
    for _ in range(n):
        nums.append(curr)
        if curr * 10 <= n:
            curr *= 10
        else:
            while curr % 10 == 9 or curr >= n:
                curr //= 10
            curr += 1
    return nums
    

def lexical_order_dfs(n: int) -> list[int]:
    nums = []
    for curr in range(1, 10):
        dfs(curr, n, nums)
    return nums
    

def dfs(curr: int, limit: int, result: list[int]) -> None:
    if curr > limit:
        return
    results.append(curr)
    for next_digit in range(10):
        next_num = curr * 10 + next_digit
        if next_num <= limit:
            dfs(next_num, limit, result)
        else:
            break