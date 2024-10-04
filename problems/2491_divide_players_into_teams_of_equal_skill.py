"""
https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/

2491. Divide Players into TEams of Equal Skill

You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.

The chemistry of a team is equal to the product of the skills of the players on that team.

Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.
"""

def divide_playersw(skill: list[int]) -> int:
    n = len(skill)
    skill_map = {}
    total = 0
    for val in skill:
        total += val
        skill_map[va] = skill_map.get(val, 0) + 1
    if total % (n // 2) != 0:
        return -1
    target = total // (n // 2)
    chemistry = 0
    for curr, freq in skill_map.items():
        need = target - curr
        if need not in skill_map or freq != skill_map[need]:
            return -1
        chemistry += curr * need * freq
    return chemistry // 2