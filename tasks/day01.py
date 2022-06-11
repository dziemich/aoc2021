from typing import Tuple

file = '../inputs/day01.txt'


def trim(str):
    return str.strip()


def part1():
    counter = 0
    with open(file) as f:
        raw_lines = f.read().split("\n")
        lines = list(map(lambda n: int(n), raw_lines))
        curr = lines[0]
        for i in range(1, len(lines)):
            if lines[i] > curr:
                counter += 1
            curr = int(lines[i])
    print(counter)


# part2
def part2():
    counter = 0
    with open(file) as f:
        raw_lines = f.read().split("\n")
        lines = list(map(lambda n: int(n), raw_lines))
        curr = sum(lines[i] for i in range(0, 3))
        for i in range(3, len(lines)):
            next = curr - lines[i - 3] + lines[i]
            if curr < next:
                counter += 1
            curr = next
    print(counter)


# part 1
if __name__ == '__main__':
    part1()
    print('====')
    part2()
