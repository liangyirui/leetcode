"""
https://leetcode.com/problems/most-beautiful-item-for-each-query/description/

You are given a 2D integer array items where items[i] = [pricei, beautyi] denotes the price and beauty of an item respectively.

You are also given a 0-indexed integer array queries. For each queries[j], you want to determine the maximum beauty of an item whose price is less than or equal to queries[j]. If no such item exists, then the answer to this query is 0.

Return an array answer of the same length as queries where answer[j] is the answer to the jth query.
"""

def maximum_beauty(items: list[list[int]], queries: list[int]) -> list[int]:
    items.sort(key=lambda x: x[0])
    n = len(queries)
    ans = [0] * n
    max_beauty = 0
    for item in items:
        max_beauty = max(max_beauty, item[1])
        item[1] = max_beauty
    for i, query in enumerate(queries):
        max_beauty = 0
        lo, hi = 0, len(items) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if items[mid][0] > query:
                hi = mid - 1
            else:
                max_beauty = max(max_beauty, items[mid][1])
                lo = mid + 1
        ans[i] = max_beauty
    return ans
