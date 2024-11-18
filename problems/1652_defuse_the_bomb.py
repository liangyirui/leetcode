"""
https://leetcode.com/problems/defuse-the-bomb/description/
You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.

As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!
"""


def decrypt(code: list[int], k: int) -> list[int]:
    n = len(code)
    ans = [0] * n
    if k == 0:
        return ans
    start, end = 1, k
    curr_sum = 0
    if k < 0:
        start = n - abs(k)
        end = n - 1
    for i in range(start, end + 1):
        curr_sum += code[i]
    for i in range(n):
        ans[i] = curr_sum
        curr_sum -= code[start % n]
        curr_sum += code[(end + 1) % n]
        start += 1
        end += 1
    return ans


if __name__ == "__main__":
    code = [5, 7, 1, 4]
    k = 3
    print(decrypt(code, k))
