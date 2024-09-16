"""
https://leetcode.com/problems/minimum-time-difference/description/

Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time points in the list.
"""

def find_min_difference(time_points: list[str]) -> int:
    minutes = [False] * 1440
    for time in time_points:
        h, m = map(int, time.split(":"))
        min_time = h * 60 + m
        if minutes[min_time]:
            return 0
        minutes[min_time] = True
        
    prev_index = first_index = last_index = min_diff = 1440
    for i in range(1440):
        if not minutes[i]:
            continue
        if prev_index != 1440:
            min_diff = min(min_diff, i - prev_index)
        prev_index = i
        if first_index == 1440:
            first_index = i
        last_index = i
    return min(min_diff, 1440 - last_index + first_index)