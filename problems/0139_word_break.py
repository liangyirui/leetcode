"""
https://leetcode.com/problems/word-break/description/

139. Word Break
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""


def word_break(s: str, word_dict: list[str]) -> bool:
    n = len(s)
    words = set(word_dict)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[n]


if __name__ == "__main__":
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(word_break(s, wordDict))
