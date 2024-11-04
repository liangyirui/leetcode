"""
https://leetcode.com/problems/string-compression-iii/description/

Given a string word, compress it using the following algorithm:

Begin with an empty string comp. While word is not empty, use the following operation:
Remove a maximum length prefix of word made of a single character c repeating at most 9 times.
Append the length of the prefix followed by c to comp.
Return the string comp.
"""


def compressed_string(word: str) -> str:
    n = len(word)
    i = j = 0
    count = 0
    comp = []
    while j < n:
        count = 0
        while j < n and word[j] == word[i] and count < 9:
            j += 1
            count += 1
        comp.append(str(count) + word[i])
        i = j
    return "".join(comp)
