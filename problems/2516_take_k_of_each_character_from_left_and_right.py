"""
https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/description/

You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.
Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.
"""


def take_characters(s: str, k: int) -> int:
    count = [0] * 3
    n = len(s)
    for ch in s:
        count[ord(ch) - ord("a")] += 1
    if min(count) < k:
        return -1
    window = [0] * 3
    left = 0
    max_window = 0
    for right, ch in enumerate(s):
        window[ord(ch) - ord("a")] += 1
        while left <= right and (
            count[0] - window[0] < k
            or count[1] - window[1] < k
            or count[2] - window[2] < k
        ):
            window[ord(s[left]) - ord("a")] -= 1
            left += 1
        max_window = max(max_window, right - left + 1)
    return n - max_window


if __name__ == "__main__":
    s = "aabaaaacaabc"
    k = 2
    print(take_characters(s, k))
