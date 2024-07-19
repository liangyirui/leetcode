"""
https://leetcode.com/problems/course-schedule-ii/description/

210. Course Schedule II

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
"""

from collections import deque


def find_order(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    adj = [[] for _ in range(numCourses)]
    for v, w in prerequisites:
        adj[w].append(v)

    marked = [False] * numCourses
    on_stack = [False] * numCourses
    order = []
    for course in range(numCourses):
        if not dfs(adj, course, order, marked, on_stack):
            return []
    return order[::-1]


def dfs(
    adj: list[list[int]],
    v: int,
    order: list[int],
    marked: list[bool],
    on_stack: list[bool],
) -> bool:
    if on_stack[v]:
        return False
    if marked[v]:
        return True
    marked[v] = True
    on_stack[v] = True
    for w in adj[v]:
        if not dfs(adj, w, order, marked, on_stack):
            return False
    order.append(v)
    on_stack[v] = False
    return True


def bfs(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    adj = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses
    for v, w in prerequisites:
        adj[w].append(v)
        indegree[v] += 1

    queue = deque()
    order = []
    for course, degree in enumerate(indegree):
        if degree == 0:
            queue.append(course)

    while queue:
        v = queue.popleft()
        order.append(v)
        for w in adj[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                queue.append(w)
    if len(order) != numCourses:
        return []
    return order


if __name__ == "__main__":
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    order_dfs = find_order(numCourses, prerequisites)
    print(order_dfs)
    order_bfs = bfs(numCourses, prerequisites)
    print(order_bfs)
