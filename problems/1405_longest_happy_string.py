"""
https://leetcode.com/problems/longest-happy-string/description/

1405. Longest Happy String

A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.
"""

import heapq

def longest_diverse_string(a: int, b: int, c: int) -> str:
    pq = []
    if a > 0:
        heapq.heappush(pq, (-a, 'a'))
    if b > 0:
        heapq.heappush(pq, (-b, 'b'))
    if c > 0:
        heapq.heappush(pq, (-c, 'c'))
    sb = []
    while pq:
        first, ch1 = heapq.heappop(pq)
        if len(sb) >= 2 and result[-1] == result[-2] == ch1:
            if not pq:
                break
            second, ch2 = heapq.heappop(pq)
            sb.append(ch2)
            second += 1
            if second != 0:
                heapq.heappush(pq, (second, ch2))
            heapq.heappush(pq, (first, ch1))
        else:
            sb.append(ch1)
            first += 1
            if first != 0:
                heapq.heappush(pq, (first, ch1))
    return ''.join(sb)