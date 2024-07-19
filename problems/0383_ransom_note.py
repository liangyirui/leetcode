"""
https://leetcode.com/problems/ransom-note/description/

383. Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
"""


def can_construct(ransom_note: str, magazine: str) -> bool:
    str_map: list[int] = [0] * 26
    for ch in magazine:
        str_map[ord(ch) - ord("a")] += 1

    for ch in ransom_note:
        num = ord(ch) - ord("a")
        str_map[num] -= 1
        if str_map[num] < 0:
            return False
    return True


if __name__ == "__main__":
    ransom_note = "aa"
    magazine = "ab"
    print(can_construct(ransom_note, magazine))
