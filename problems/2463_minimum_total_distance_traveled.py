"""
https://leetcode.com/problems/minimum-total-distance-traveled/description/

There are some robots and factories on the X-axis. You are given an integer array robot where robot[i] is the position of the ith robot. You are also given a 2D integer array factory where factory[j] = [positionj, limitj] indicates that positionj is the position of the jth factory and that the jth factory can repair at most limitj robots.

The positions of each robot are unique. The positions of each factory are also unique. Note that a robot can be in the same position as a factory initially.

All the robots are initially broken; they keep moving in one direction. The direction could be the negative or the positive direction of the X-axis. When a robot reaches a factory that did not reach its limit, the factory repairs the robot, and it stops moving.

At any moment, you can set the initial direction of moving for some robot. Your target is to minimize the total distance traveled by all the robots.

Return the minimum total distance traveled by all the robots. The test cases are generated such that all the robots can be repaired.

Note that

All robots move at the same speed.
If two robots move in the same direction, they will never collide.
If two robots move in opposite directions and they meet at some point, they do not collide. They cross each other.
If a robot passes by a factory that reached its limits, it crosses it as if it does not exist.
If the robot moved from a position x to a position y, the distance it moved is |y - x|.
"""

def minimum_total_distance(robot: list[int], factory: list[list[int]]) -> int:
    robot.sort()
    factory.sort()
    factory_pos = []
    for f in factory:
        factory_pos.extend([f[0]] * f[1])
    m = len(robot)
    n = len(factory_pos)
    memo = [[None] * (n + 1) for _ in range(m + 1)]
    return dp(robot, 0, factory_pos, 0, memo)
    
def dp(robot: list[int], robot_idx: int, factory_pos: list[int], factory_idx: int, memo: list[list[int | None]]) -> int:
    if memo[robot_idx][factory_idx] is not None:
        return memo[robot_idx][factory_idx]
    if robot_idx == len(robot):
        memo[robot_idx][factory_idx] = 0
        return 0
    if factory_idx == len(factory_pos):
        memo[robot_idx][factory_idx] = int(1e12)
        return int(1e12)
    assign = abs(robot[robot_idx] - factory_pos[factory_idx]) + dp(robot, robot_idx + 1, factory_pos, factory_idx + 1, memo)
    skip = dp(robot, robot_idx, factory_pos, factory_idx + 1, memo)
    memo[robot_idx][factory_idx] = min(assign, skip)
    return memo[robot_idx][factory_idx]