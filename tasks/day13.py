import copy
from operator import itemgetter

file = '../inputs/day13.txt'


def part1():
    with open(file) as f:
        raw_lines = f.read().split("\n")
        cnt = 0
        line = raw_lines[cnt]
        points = set()
        while len(line) > 0 and line[0].isdigit():
            x, y = line.split(",")
            points.add((int(x), int(y)))
            cnt += 1
            line = raw_lines[cnt]

        splits = raw_lines[cnt + 1:]
        lns = []
        for s in splits:
            iter_set = copy.deepcopy(points)
            _, f = s.split("=")
            fold = int(f)
            if 'x' in s:
                # do a vertical
                for p in iter_set:
                    if p[0] > fold:
                        points.remove(p)
                        points.add((2 * fold - p[0], p[1]))
            else:
                for p in iter_set:
                    if p[1] > fold:
                        points.remove(p)
                        points.add((p[0], 2 * fold - p[1]))
            lns.append(len(points))
        print(lns)


def part2():
    with open(file) as f:
        raw_lines = f.read().split("\n")
        cnt = 0
        line = raw_lines[cnt]
        points = set()
        while len(line) > 0 and line[0].isdigit():
            x, y = line.split(",")
            points.add((int(x), int(y)))
            cnt += 1
            line = raw_lines[cnt]

        splits = raw_lines[cnt + 1:]

        for s in splits:
            iter_set = copy.deepcopy(points)
            _, f = s.split("=")
            fold = int(f)
            if 'x' in s:
                # do a vertical
                for p in iter_set:
                    if p[0] > fold:
                        points.remove(p)
                        points.add((2 * fold - p[0], p[1]))
            else:
                for p in iter_set:
                    if p[1] > fold:
                        points.remove(p)
                        points.add((p[0], 2 * fold - p[1]))

    l = list(points)
    mv = max(l, key=itemgetter(0))[0]
    mh = max(l, key=itemgetter(0))[1]

    for i in range(mh + 1):
        s = ""
        for j in range(mv + 1):
            if (j, i) in points:
                s += "&"
            else:
                s += " "
        print(s)


if __name__ == '__main__':
    part1()
    print('====')
    part2()
