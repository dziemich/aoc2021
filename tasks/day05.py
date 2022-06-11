from collections import Counter
from itertools import takewhile

fily = '../inputs/day05.txt'


def part1():
    with open(fily) as f:
        raw_lines = f.read().split("\n")
        tuples = []

        for line in raw_lines:
            l, r = line.split("->")
            lx, ly = l.strip().split(",")
            rx, ry = r.strip().split(",")

            if lx != rx and ly != ry:
                continue

            rx = int(rx)
            ry = int(ry)
            lx = int(lx)
            ly = int(ly)

            new_tuples = create_tuples_vh(lx, ly, rx, ry)
            tuples += new_tuples

        cnt = Counter()

        for entry in tuples:
            cnt[entry] += 1

        above_threshold = dict(takewhile(lambda e: e[1] >= 2, cnt.most_common()))
        print(len(list(above_threshold)))


def part2():
    with open(fily) as f:
        raw_lines = f.read().split("\n")
        tuples = []

        for line in raw_lines:
            l, r = line.split("->")
            lx, ly = l.strip().split(",")
            rx, ry = r.strip().split(",")

            rx = int(rx)
            ry = int(ry)
            lx = int(lx)
            ly = int(ly)

            if lx != rx and ly != ry:
                tuples += create_tuples_diag(lx, ly, rx, ry)
            else:
                tuples += create_tuples_vh(lx, ly, rx, ry)

        cnt = Counter()

        for entry in tuples:
            cnt[entry] += 1

        above_threshold = dict(takewhile(lambda e: e[1] >= 2, cnt.most_common()))
        print(len(list(above_threshold)))


def create_tuples_vh(lx, ly, rx, ry):
    tuples = []
    if lx > rx:
        tmp = rx
        rx = lx
        lx = tmp
    if ly > ry:
        tmp = ry
        ry = ly
        ly = tmp

    for i in range(0, rx - lx):
        tuples.append((lx + i, ry))
    for i in range(0, ry - ly):
        tuples.append((rx, ly + i))
    tuples.append((rx, ry))
    return tuples


def create_tuples_diag(lx, ly, rx, ry):
    tuples = []

    # 0,0 -> 8,8 but also 8,8 -> 0,0
    if (lx < rx and ly < ry) or (lx > rx and ly > ry):
        if lx > rx and ly > ry:
            tmp = rx
            rx = lx
            lx = tmp
            tmp = ry
            ry = ly
            ly = tmp

        for i in range(0, rx - lx):
            tuples.append((lx + i, ly + i))
    # 8,0 -> 0,8 but also 0,8 -> 8,0
    else:
        if lx > rx:
            tmp = rx
            rx = lx
            lx = tmp
            tmp = ry
            ry = ly
            ly = tmp

        for i in range(0, abs(lx - rx)):
            tuples.append((lx + i, ly - i))
    tuples.append((rx, ry))
    return tuples


# part 1
if __name__ == '__main__':
    part1()
    print('====')
    part2()
