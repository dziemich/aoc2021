from collections import Counter

file = '../inputs/day07.txt'


def part1():
    def calc1(a, b):
        return abs(a - b)

    calc_fuel(calc1)


def part2():
    def calc2(a, b):
        n = abs(a - b)
        res = ((1 + n) / 2) * n
        return res

    calc_fuel(calc2)


def calc_fuel(fn):
    with open(file) as f:
        line = list(map(int, f.read().split(",")))
        occ = Counter(line)
        fuel = Counter()
        max_v = max(line)
        min_v = min(line)

        for i in range(min_v, max_v):
            for k, v in occ.items():
                diff = fn(i, k)
                fuel[i] += diff * v
    print(min(list(fuel.values())))


# part 1
if __name__ == '__main__':
    part1()
    print('====')
    part2()
