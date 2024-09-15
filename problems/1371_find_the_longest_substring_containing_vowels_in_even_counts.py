"""
https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description/

1371. Find the Longest Substring Containing Vowels in Even Counts

Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.
"""

def find_the_longest_substring(s: str) -> int:
    prefix_xor = 0
    char_map = [0] * 26
    char_map[ord('a') - ord('a')] = 1
    char_map[ord('e') - ord('a')] = 2
    char_map[ord('i') - ord('a')] = 4
    char_map[ord('o') - ord('a')] = 8
    char_map[ord('u') - ord('a')] = 16
    first_occurrence = [-1] * 32 # total number of prefix_xor states
    longest = 0
    for i, ch in enumerate(s):
        prefix_xor ^= char_map[ord(ch) - ord('a')]
        if prefix_xor != 0 and first_occurrence[prefix_xor] == -1:
            first_occurrence[prefix_xor] = i
        longest = max(longest, i - first_occurrence[prefix_xor])
    return longest