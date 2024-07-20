"""
https://leetcode.com/problems/crawler-log-folder/description/

1598. Crawler Log Folder

The Leetcode file system keeps a log each time some user performs a change folder operation.

The operations are described below:

"../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
"./" : Remain in the same folder.
"x/" : Move to the child folder named x (This folder is guaranteed to always exist).
You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

The file system starts in the main folder, then the operations in logs are performed.

Return the minimum number of operations needed to go back to the main folder after the change folder operations.
"""


def min_operations(logs: list[str]) -> int:
    level = 0
    for log in logs:
        if log == "../":
            level = max(0, level - 1)
        elif log != "./":
            level += 1
    return level


def min_operations_stack(logs: list[str]) -> int:
    stack = []
    for log in logs:
        if log == "../":
            if stack:
                stack.pop()
        elif log != "./":
            stack.append(log)
    return len(stack)


if __name__ == "__main__":
    logs = ["d1/", "d2/", "./", "d3/", "../", "d31/"]
    print(min_operations(logs))
