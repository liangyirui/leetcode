"""
https://leetcode.com/problems/reverse-words-in-a-string/description/

Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
"""


def reverse_words(s: str) -> str:
    words = []
    i = 0
    inword = False
    for j, ch in enumerate(s):
        if not inword and ch != " ":
            inword = True
            i = j
        elif inword and ch == " ":
            words.append(s[i:j])
            inword = False
    if inword:
        words.append(s[i:])
    reverse_list(words, 0, len(words) - 1)
    return " ".join(words)


def reverse_list(lst: list, i: int, j: int) -> None:
    if i >= j:
        return
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1


if __name__ == "__main__":
    s = " the sky is blue   "
    print(reverse_words(s))
