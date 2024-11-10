"""
https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/description/

You are given an array nums of non-negative integers and an integer k.

An array is called special if the bitwise OR of all of its elements is at least k.

Return the length of the shortest special non-empty subarray of nums, or return -1 if no special subarray exists.
"""
def minimum_subarray_length(nums: list[int], k: int) -> int:
    if k == 0:
        return 1
    n = len(nums)
    ans = n + 1
    lo = 0
    bit_or = 0
    bit_count = [0] * 32
    for hi, num in enumerate(nums):
        bit_or |= num
        for i in range(32):
            bit_count[i] += (num >> i) & 1
        while lo <= hi and bit_or >= k:
            ans = min(ans, hi - lo + 1)
            bit_or = 0
            for i in range(32):
                bit_count[i] -= (nums[lo] >> i) & 1
                if bit_count[i] > 0:
                    bit_or |= 1 << i
            lo += 1
    return ans if ans <= n else -1
