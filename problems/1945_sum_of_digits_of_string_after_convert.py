"""
https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

1945. Sum of Digits of String after Convert

You are given a string s consisting of lowercase English letters, and an integer k.
First, convert s into an integer by replacing each letter with its position in the alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26). Then, transform the integer by replacing it with the sum of its digits. Repeat the transform operation k times in total.
For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:
Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
Transform #2: 17 ➝ 1 + 7 ➝ 8
Return the resulting integer after performing the operations described above.
"""

def get_lucky(s: str, k: int) -> int:
    sb: list[str] = []
    for ch in s:
        num = ord(ch) - ord('a') + 1
        sb.append(str(num))
    ans = int(''.join(sb))
    for _ in range(k):
        ans = transform(ans)
    return ans
    

def transform(num: int) -> int:
    ans = 0
    while num > 0:
        ans += num % 10
        num //= 10
    return ans