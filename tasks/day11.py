import copy
from collections import Counter
import heapq

file = '../inputs/day11.txt'


def neighs(i, j):
    return [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i + 1, j + 1), (i - 1, j - 1), (i + 1, j - 1),
            (i - 1, j + 1)]


def part1():
    with open(file) as f:
        raw_lines = f.read().split("\n")

        grid = [[int(ch) for ch in line] for line in raw_lines]
        steps = 100

    above_nines_seen = set()

    def is_inside(i, j):
        return 0 <= i < len(grid) and 0 <= j < len(grid[i])

    def dfs(i, j):

        for ni, nj in neighs(i, j):

            if (ni, nj) == (i, j):
                continue

            if is_inside(ni, nj):
                grid[ni][nj] = min(10, grid[ni][nj] + 1)

                if (ni, nj) not in above_nines_seen and grid[ni][nj] >= 10:
                    above_nines_seen.add((ni, nj))
                    dfs(ni, nj)

    flashes = 0
    for step in range(steps):
        above_nines_seen = set()
        # increment energy
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] += 1

        # account for adjacent activations
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                h = grid[i][j]
                if (i, j) not in above_nines_seen and h >= 10:
                    above_nines_seen.add((i, j))
                    dfs(i, j)

        # flash
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] >= 10:
                    grid[i][j] = 0
                    flashes += 1
    print(flashes)


def part2():
    with open(file) as f:
        raw_lines = f.read().split("\n")

        grid = [[int(ch) for ch in line] for line in raw_lines]
        steps = 100

    above_nines_seen = set()

    def is_inside(i, j):
        return 0 <= i < len(grid) and 0 <= j < len(grid[i])

    def dfs(i, j):

        for ni, nj in neighs(i, j):

            if (ni, nj) == (i, j):
                continue

            if is_inside(ni, nj):
                grid[ni][nj] = min(10, grid[ni][nj] + 1)

                if (ni, nj) not in above_nines_seen and grid[ni][nj] >= 10:
                    above_nines_seen.add((ni, nj))
                    dfs(ni, nj)

    cnt = 1
    while True:
        above_nines_seen = set()
        # increment energy
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] += 1

        # account for adjacent activations
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                h = grid[i][j]
                if (i, j) not in above_nines_seen and h >= 10:
                    above_nines_seen.add((i, j))
                    dfs(i, j)

        # flash
        cf = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] >= 10:
                    grid[i][j] = 0
                    cf += 1
        if cf == 100:
            print(cnt)
            return
        cnt += 1


if __name__ == '__main__':
    part1()
    print('====')
    part2()
