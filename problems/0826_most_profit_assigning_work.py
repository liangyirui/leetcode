"""
https://leetcode.com/problems/most-profit-assigning-work/description/

826. Most Profit Assigning Work

You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).

Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.

Return the maximum profit we can achieve after assigning the workers to the jobs.
"""


def max_profit_assignment(
    difficulty: list[int], profit: list[int], worker: list[int]
) -> int:
    assignment = sorted(zip(difficulty, profit))
    worker.sort()
    n = len(assignment)
    max_profit = curr_profit = 0
    i = 0
    for w in worker:
        while i < n and w >= assignment[i][0]:
            curr_profit = max(curr_profit, assignment[i][1])
            i += 1
        max_profit += curr_profit
    return max_profit


if __name__ == "__main__":
    difficulty = [2, 4, 6, 8, 20]
    profit = [10, 20, 30, 40, 50]
    worker = [4, 5, 6, 7]
    print(f"Maximum profit is {max_profit_assignment(difficulty, profit, worker)}")
