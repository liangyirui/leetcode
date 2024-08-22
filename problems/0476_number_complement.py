"""
https://leetcode.com/problems/number-complement/description/

The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.
"""


def find_complement(num: int) -> int:
    bitmask = num
    bitmask |= bitmask >> 1
    bitmask |= bitmask >> 2
    bitmask |= bitmask >> 4
    bitmask |= bitmask >> 8
    bitmask |= bitmask >> 16
    return bitmask ^ num


def find_complement_2(num: int) -> int:
    length = 0
    i = num
    while i > 0:
        length += 1
        i >>= 1
    return ((1 << length) - 1) ^ num


if __name__ == "__main__":
    num = 5
    print(find_complement(num))
    print(find_complement_2(num))
