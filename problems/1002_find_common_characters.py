"""
https://leetcode.com/problems/find-common-characters/description/

1002. Find Common Characters
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
"""

from collections import Counter


def common_chars(words: list[str]) -> list[str]:
    common_letters: Counter = Counter(words[0])
    for word in words:
        curr_letters = Counter(word)
        for ch in common_letters:
            common_letters[ch] = min(common_letters[ch], curr_letters[ch])
    return list(common_letters.elements())


if __name__ == "__main__":
    words = ["bella", "label", "roller"]
    print(common_chars(words))
