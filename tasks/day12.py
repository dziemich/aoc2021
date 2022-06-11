import copy
from collections import defaultdict
import heapq

file = '../inputs/day12.txt'


def part1():
    c = 0
    with open(file) as f:
        raw_lines = f.read().split("\n")

        graph = defaultdict(list)
        for l in raw_lines:
            a, b = l.split('-')
            graph[a].append(b)
            graph[b].append(a)

        def dfs(v, seen):
            nonlocal c
            if v == 'end':
                c += 1
                return

            for nv in graph[v]:
                if nv.isupper() or nv not in seen:
                    cp = copy.deepcopy(seen)
                    cp.add(nv)
                    dfs(nv, cp)

        dfs('start', {"start"})
        print(c)


def part2():
    c = 0
    with open(file) as f:
        raw_lines = f.read().split("\n")

        graph = defaultdict(list)
        for l in raw_lines:
            a, b = l.split('-')
            graph[a].append(b)
            graph[b].append(a)

        total = set()

        def dfs(v, seen, small_seen):
            nonlocal c
            if v == 'end':
                c += 1
                return

            for nv in graph[v]:
                if nv.isupper() or nv not in seen:
                    cp = copy.deepcopy(seen)
                    cp.add(nv)
                    dfs(nv, cp, small_seen)

                elif not small_seen and nv != 'start' and nv != 'end':
                    cp = copy.deepcopy(seen)
                    cp.add(nv)
                    dfs(nv, cp, True)

    dfs('start', {"start"}, False)
    print(c)


if __name__ == '__main__':
    part1()
    print('====')
    part2()
