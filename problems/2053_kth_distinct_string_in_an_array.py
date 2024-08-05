"""
https://leetcode.com/problems/kth-distinct-string-in-an-array/

2053. Kth Distinct String in an Array

A distinct string is a string that is present only once in an array.
Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".
Note that the strings are considered in the order in which they appear in the array.
"""

from collections import Counter


def kth_distinct(arr: list[str], k: int) -> str:
    freq = Counter(arr)
    for s in arr:
        if freq[s] == 1:
            k -= 1
        if k == 0:
            return s
    return ""


if __name__ == "__main__":
    arr = ["d", "b", "c", "b", "c", "a"]
    k = 2
    print(kth_distinct(arr, k))
