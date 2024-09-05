"""
https://leetcode.com/problems/walking-robot-simulation/description/

874. Walking Robot Simulation

A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot can receive a sequence of these three possible types of commands:

-2: Turn left 90 degrees.
-1: Turn right 90 degrees.
1 <= k <= 9: Move forward k units, one unit at a time.
Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). If the robot runs into an obstacle, then it will instead stay in its current location and move on to the next command.

Return the maximum Euclidean distance that the robot ever gets from the origin squared (i.e. if the distance is 5, return 25).

Note:

North means +Y direction.
East means +X direction.
South means -Y direction.
West means -X direction.
There can be obstacle in [0,0].
"""

def robot_simulation(commands: list[int], obstacles: list[list[int]]) -> int:
    obstacles_set = {(x, y) for x, y in obstacles}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x = y = 0
    dist = 0
    direction = 0
    for command in commands:
        if command == -1:
            direction = (direction + 1) % 4
        elif command == -2:
            direction = (direction + 3) % 4
        else:
            dx, dy = directions[dicrection]
            for _ in range(command):
                next_x, next_y = x + dx, y + dy
                if (next_x, next_y) in obstacles_set:
                    break
                x, y = next_x, next_y
            dist = max(dist, x * x + y * y)
    return dist
    
if __name__ == "__main__":
    commands = [4, -1, 4, -2, 4]
    obstacles = [[2, 4]]
    print(robot_simulation(commands, obstacles))