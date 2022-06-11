from collections import Counter

file = '../inputs/day06.txt'


def part1():
    count_fish(80)


def part2():
    count_fish(256)


def count_fish(days):
    total = 0
    with open(file) as f:
        line = list(map(int, f.read().split(",")))
        c = Counter(line)
        for k, v in c.items():
            total += count(k, days) * v
    print(total)


def count(seed, d):
    prev = Counter([seed])
    for i in range(0, d):
        curr = Counter()

        for k, v in prev.items():
            if k == 0:
                curr[6] += v
                curr[8] += v
            else:
                curr[k - 1] += v
        prev = curr
    return sum(prev.values())


# part 1
if __name__ == '__main__':
    part1()
    print('====')
    part2()
