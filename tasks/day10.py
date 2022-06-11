import copy
from collections import Counter
import heapq

file = '../inputs/day10.txt'

from collections import deque

stack = deque()


def part1():
    with open(file) as f:
        raw_lines = f.read().split("\n")

        def get_point(line):
            stack = []
            matches = {'(': ')', '[': ']', '{': '}', '<': '>'}

            points = {
                ')': 3,
                ']': 57,
                '}': 1197,
                '>': 25137,
            }

            for ch in line:
                if ch in matches.keys():
                    stack.append(ch)
                    continue

                top = stack.pop()
                if matches[top] != ch:
                    return points[ch]
            return 0

        total = 0
        for line in raw_lines:
            total += get_point(line)

        print(total)


def part2():
    with open(file) as f:
        raw_lines = f.read().split("\n")

        def get_point(line):
            stack = []
            matches = {'(': ')', '[': ']', '{': '}', '<': '>'}

            points = {
                ')': 1,
                ']': 2,
                '}': 3,
                '>': 4,
            }

            for ch in line:
                if ch in matches.keys():
                    stack.append(ch)
                    continue

                top = stack.pop()
                if matches[top] != ch:
                    return -1

            total = 0
            for i in range(0, len(stack)):
                total *= 5
                top = stack.pop()
                total += points[matches[top]]
            return total

        results = []
        for line in raw_lines:
            res = get_point(line)
            if res != -1:
                results.append(res)

        results.sort()

        print(results[len(results) // 2])

if __name__ == '__main__':
    # part1()
    print('====')
    part2()
