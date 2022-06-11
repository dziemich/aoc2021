file = '../inputs/day16.txt'


def to_binary(line):
    bits = []
    for ch in line:
        v = int(ch, 16)
        bs = bin(v)[2:]
        bs = '0' * (4 - len(bs)) + bs
        for b in bs:
            bits.append(b)
    return ''.join(bits)


def part1():
    with open(file) as f:
        input = f.read().split("\n")[0].strip()
        binary = to_binary(input)

        ver_num = 0

        def parse(pos):
            nonlocal binary
            nonlocal ver_num

            version = binary[pos: pos + 3]
            v = int(version, 2)
            ver_num += v
            type = binary[pos + 3: pos + 6]
            t = int(type, 2)

            if t == 4:
                marker = pos + 6
                while binary[marker] == '1':
                    marker += 5
                marker += 5
                return marker
            else:
                ltid = binary[pos + 6]
                if ltid == '0':
                    substr = binary[pos + 7: pos + 7 + 15]
                    total_len = int(substr, 2)
                    marker = pos + 7 + 15
                    while marker < pos + 7 + 15 + total_len:
                        marker = parse(marker)
                    return marker
                else:
                    substr = binary[pos + 7: pos + 7 + 11]
                    sub_count = int(substr, 2)
                    marker = pos + 7 + 11
                    for i in range(sub_count):
                        marker = parse(marker)
                    return marker

        parse(0)
        print(ver_num)


def part2():
    with open(file) as f:
        input = f.read().split("\n")[0].strip()
        binary = to_binary(input)

        def parse(pos):
            nonlocal binary

            version = binary[pos: pos + 3]
            v = int(version, 2)
            type = binary[pos + 3: pos + 6]
            t = int(type, 2)

            if t == 4:
                c = ""
                marker = pos + 6
                while binary[marker] == '1':
                    c += binary[marker + 1: marker + 5]
                    marker += 5
                c += binary[marker + 1: marker + 5]
                marker += 5
                res = int(c, 2)
                return marker, res
            else:
                ltid = binary[pos + 6]
                arr = []
                if ltid == '0':
                    substr = binary[pos + 7: pos + 7 + 15]
                    total_len = int(substr, 2)
                    marker = pos + 7 + 15
                    while marker < pos + 7 + 15 + total_len:
                        m, r = parse(marker)
                        marker = m
                        arr.append(r)
                else:
                    substr = binary[pos + 7: pos + 7 + 11]
                    sub_count = int(substr, 2)
                    marker = pos + 7 + 11
                    for i in range(sub_count):
                        m, r = parse(marker)
                        marker = m
                        arr.append(r)
                res = 0
                if t == 0:
                    res = sum(arr)
                if t == 1:
                    res = 1
                    for v in arr:
                        res *= v
                if t == 2:
                    res = min(arr)
                if t == 3:
                    res = max(arr)
                if t == 5:
                    res = 1 if arr[0] > arr[1] else 0
                if t == 6:
                    res = 1 if arr[0] < arr[1] else 0
                if t == 7:
                    res = 1 if arr[0] == arr[1] else 0
                return marker, res

        m, r = parse(0)
        print(r)


# def part2():
#     with open(file) as f:
#         raw_lines = f.read().split("\n")
#         grid = [[int(ch) for ch in line] for line in raw_lines]
#         dijk(enlarge(grid, 5))


if __name__ == '__main__':
    part1()
    print('====')
    part2()
