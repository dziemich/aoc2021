import copy
import heapq
from operator import itemgetter
from collections import Counter, defaultdict

file = '../inputs/day15.txt'


def neighs(i, j):
    return [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]


def enlarge(G, cnt):
    R0, C0 = len(G), len(G[0])
    G2 = [[0 for _ in range(C0 * cnt)] for _ in range(R0 * cnt)]
    for ir in range(cnt):
        for ic in range(cnt):
            for r in range(R0):
                for c in range(C0):
                    ov = G[r][c]
                    nv = 1 + (ov + ir + ic - 1) % 9
                    G2[ir * R0 + r][ic * C0 + c] = nv
    return G2


def part1():
    with open(file) as f:
        raw_lines = f.read().split("\n")
        grid = [[int(ch) for ch in line] for line in raw_lines]
        dijk(grid)


def part2():
    with open(file) as f:
        raw_lines = f.read().split("\n")
        grid = [[int(ch) for ch in line] for line in raw_lines]
        dijk(enlarge(grid, 5))


def dijk(grid):
    def is_inside(i, j):
        return 0 <= i < len(grid) and 0 <= j < len(grid[i])

    visited = set()
    end = (len(grid) - 1, len(grid[0]) - 1)
    pq = []
    heapq.heappush(pq, (0, (0, 0)))

    distances = defaultdict(lambda: float('inf'))

    while pq:
        cost, node = heapq.heappop(pq)
        visited.add(node)

        if node == end:
            print(cost)
            return

        for ni, nj in neighs(node[0], node[1]):
            if (ni, nj) not in visited and is_inside(ni, nj):
                new_cost = cost + grid[ni][nj]
                if distances[(ni, nj)] > new_cost:
                    distances[(ni, nj)] = new_cost
                    heapq.heappush(pq, (new_cost, (ni, nj)))


# def part1():
#     with open(file) as f:
#         raw_lines = f.read().split("\n")
#         grid = [[int(ch) for ch in line] for line in raw_lines]
#         minimum = 99999999999
#
#         end = (len(grid) - 1, len(grid[0]) - 1)
#
#         def is_inside(i, j):
#             return 0 <= i < len(grid) and 0 <= j < len(grid[i])
#
#         def dfs(i, j, curr, seen):
#             nonlocal end
#             nonlocal minimum
#             if curr > minimum:
#                 return
#             if (i, j) == end:
#                 minimum = min(minimum, curr)
#                 return
#
#             for ni, nj in neighs(i, j):
#                 if (ni, nj) not in seen and is_inside(ni, nj):
#                     ns = copy.deepcopy(seen)
#                     ns.add((ni, nj))
#                     dfs(ni, nj, curr + grid[ni][nj], ns)
#
#         dfs(0, 0, 0, {(0, 0)})
#
#         print(minimum)


# def part2():


if __name__ == '__main__':
    part1()
    # print('====')
    part2()
