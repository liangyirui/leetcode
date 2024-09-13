"""
https://leetcode.com/problems/xor-queries-of-a-subarray/description/

You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].

For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).

Return an array answer where answer[i] is the answer to the ith query.
"""

def xor_queries(arr: list[int], queries: list[list[int]]) -> list[int]:
    prefix_xor = [0] * (len(arr) + 1)
    n = len(queries)
    result = [0] * n
    for i, val in enumerate(arr):
        prefix_xor[i + 1] = prefix_xor[i] ^ val
    for i, (l, r) in enumerate(queries):
        result[i] = prefix_xor[r + 1] ^ prefix_xor[l]
	return result