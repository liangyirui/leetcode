"""
https://leetcode.com/problems/sliding-puzzle/description/

On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.
The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].
Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

Example:
#############
# 1 # 2 # 3 #
# 4 #   # 5 #
#############
Swap the 0 and 5 in one move.
"""

from collections import deque


def sliding_puzzle(board: list[list[int]]) -> int:
    # direction map for zero's possible moves in a 1D representation of the 2x3 board
    directions = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
    initial_state = "".join([str(num) for row in board for num in row])
    target = "123450"
    queue = deque([initial_state])
    visited = set()
    moves = 0
    while queue:
        for _ in range(len(queue)):
            curr_state = queue.popleft()
            if curr_state == target:
                return moves
            zero_pos = curr_state.index("0")
            for next_pos in directions[zero_pos]:
                next_state = swap(curr_state, zero_pos, next_pos)
                if next_state in visited:
                    continue
                visited.add(next_state)
                queue.append(next_state)
        moves += 1
    return -1


def swap(state: str, i: int, j: int) -> str:
    state_list = list(state)
    state_list[i], state_list[j] = state_list[j], state_list[i]
    return "".join(state_list)


if __name__ == "__main__":
    board = [[4, 1, 2], [5, 0, 3]]
    print(sliding_puzzle(board))
