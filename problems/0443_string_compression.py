"""
https://leetcode.com/problems/string-compression/description/

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

1. If the group's length is 1, append the character to s.
2. Otherwise, append the character followed by the group's length.

The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
After you are done modifying the input array, return the new length of the array.
You must write an algorithm that uses only constant extra space.
"""


def compress(chars: list[str]) -> int:
    n = len(chars)
    i = 0
    length = 0
    while i < n:
        curr = chars[i]
        count = 0
        while i < n and chars[i] == curr:
            i += 1
            count += 1
        chars[length] = curr
        length += 1
        if count > 1:
            for ch in str(count):
                chars[length] = ch
                length += 1
    return length


if __name__ == "__main__":
    chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    print(compress(chars))
