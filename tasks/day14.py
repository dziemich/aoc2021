import copy
from operator import itemgetter
from collections import Counter, defaultdict

file = '../inputs/day14.txt'


def part1():
    with open(file) as f:
        raw_lines = f.read().split("\n")
        init = raw_lines[0]

        graph = defaultdict(list)
        for l in raw_lines[2:]:
            a, b = l.split('->')
            graph[a.strip()].append(b.strip())

        steps = 10
        for i in range(steps):
            s = ""
            for j in range(len(init) - 1):
                key = init[j:j + 2]
                if graph[key] is not None:
                    s += f"{init[j]}{graph[key][0]}"
                else:
                    s += key
                if j == len(init) - 2:
                    s += init[len(init) - 1]
            init = s

        c = Counter(list(init))
        minimum = min(c.values())
        maximum = max(c.values())
        print(maximum - minimum)


def part2():
    with open(file) as f:
        raw_lines = f.read().split("\n")
        init = raw_lines[0]

        outcomes = defaultdict(list)
        for l in raw_lines[2:]:
            a, b = l.split(' -> ')
            outcomes[a[0] + b].append(a)
            outcomes[b + a[1]].append(a)

        init_freqs = Counter()

        for o in outcomes:
            init_freqs[o] = 0

        for j in range(len(init) - 1):
            key = init[j:j + 2]
            init_freqs[key] += 1

        steps = 40
        for _ in range(steps):
            freqs = Counter()
            for p, _ in init_freqs.items():
                f = 0
                for o in outcomes[p]:
                    f += init_freqs[o]
                freqs[p] = f
            init_freqs = freqs

        c = Counter()
        for p, v in init_freqs.items():
            c[p[0]] += v
            c[p[1]] += v

        norm = [(value + 1) // 2 for value in c.values()]
        print(max(norm) - min(norm))
if __name__ == '__main__':
    part1()
    print('====')
    part2()
