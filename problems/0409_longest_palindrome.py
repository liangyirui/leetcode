"""
https://leetcode.com/problems/longest-palindrome/description/

409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest
palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome.
"""


def longest_palindrome(s: str) -> int:
    freq = [0] * 256
    count = 0
    for ch in s:
        freq[ord(ch)] += 1
    for num in freq:
        count += (num // 2) * 2
    return count if count == len(s) else count + 1


if __name__ == "__main__":
    s = "abccccdd"
    print(longest_palindrome(s))
