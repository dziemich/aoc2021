import copy
from collections import Counter
import heapq

file = '../inputs/day09.txt'


def neighs(i, j):
    return [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]


def part1():
    with open(file) as f:
        raw_lines = f.read().split("\n")

        grid = [[int(ch) for ch in line] for line in raw_lines]
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                h = grid[i][j]
                ok = True
                for ni, nj in neighs(i, j):
                    if ni >= 0 and ni < len(grid) and nj >= 0 and nj < len(grid[i]):
                        ok = ok and h < grid[ni][nj]
                if ok:
                    ans += h + 1

        print(ans)


def part2():
    with open(file) as f:
        raw_lines = f.read().split("\n")

        grid = [[int(ch) for ch in line] for line in raw_lines]
        lows = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                h = grid[i][j]
                ok = True
                for ni, nj in neighs(i, j):
                    if ni >= 0 and ni < len(grid) and nj >= 0 and nj < len(grid[i]):
                        ok = ok and h < grid[ni][nj]
                lows.append((i, j))
        Ls = []
        for i, j in lows:
            q = [(i, j)]
            seen = set(q)
            while q:
                q2 = []
                for i, j in q:
                    for ni, nj in neighs(i, j):
                        if ni >= 0 and ni < len(grid) and nj >= 0 and nj < len(grid[i]):
                            h_new = grid[ni][nj]
                            if h_new != 9 and h_new > grid[i][j]:
                                if (ni, nj) not in seen:
                                    seen.add((ni, nj))
                                    q2.append((ni, nj))
                q = q2
            Ls.append(len(seen))
        Ls.sort()
        print(Ls[-3] * Ls[-2] * Ls[-1])


# def dfs(i, j, grid, visited, curr_size):
#     if is_outside(i, j, grid):
#         return curr_size - 1
#     if grid[i][j] == 9:
#         return curr_size - 1
#     m = -1
#     for ni, nj in neighs(i, j):
#         if (ni, nj) not in visited:
#             cp = copy.deepcopy(visited)
#             cp.add((ni, nj))
#             m = max(m, dfs(ni, nj, grid, cp, curr_size + 1))
#     return m


def is_outside(i, j, grid):
    return i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0])


if __name__ == '__main__':
    part1()
    print('====')
    part2()
