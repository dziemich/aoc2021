from collections import Counter

file = '../inputs/day08.txt'


def part1():
    with open(file) as f:
        cnt = 0
        raw_lines = f.read().split("\n")
        for line in raw_lines:
            left, right = line.split('|')
            right_nums = right.split()

            for num in right_nums:
                if len(num) in [2, 3, 4, 7]:
                    cnt += 1
        print(cnt)


def part2():
    with open(file) as f:
        cnt = 0
        raw_lines = f.read().split("\n")
        for line in raw_lines:
            left, right = line.split('|')

            dict = get_dict(left.split())
            output = calc_output(dict, right.split())
            cnt += output
        print(cnt)


# SEGMENTS
#   aaa
# b     c
# b     c
#   ddd
# e     f
# e     f
#   ggg

def get_of_len(arr, num):
    a = []
    for el in arr:
        if len(el) == num:
            a.append(el)
    return a


# if not equal len, num1 should be the longer
def diff(num1, num2):
    for l in num1:
        if l not in num2:
            return l


def get_dict(input):
    mapping = {}
    # find a
    one = get_of_len(input, 2)[0]
    seven = get_of_len(input, 3)[0]
    mapping["a"] = diff(seven, one)
    # mapping[diff(seven, one)] = "a"

    # find c & f
    nums069 = get_of_len(input, 6)

    diff06 = diff(nums069[0], nums069[1])
    diff09 = diff(nums069[0], nums069[2])
    diff69 = diff(nums069[1], nums069[2])
    diff60 = diff(nums069[1], nums069[0])
    diff90 = diff(nums069[2], nums069[0])
    diff96 = diff(nums069[2], nums069[1])

    six_char_diff = [diff06, diff09, diff69, diff60, diff90, diff96]

    c = ''
    for l in six_char_diff:
        if l in one:
            c = l
    mapping["c"] = c
    mapping["f"] = one.replace(c, "").strip()
    # mapping[c] = "c"
    # mapping[one.replace(c, "").strip()] = "f"

    # find b & d
    four = get_of_len(input, 4)[0]

    d = ''
    for l in six_char_diff:
        if l in four and l not in mapping.values():
            d = l
    mapping["d"] = d
    # mapping[d] = "d"
    b = ''
    for l in four:
        if l not in mapping.values():
            b = l

    mapping["b"] = b
    # mapping[b] = "b"

    # find e
    e = ''
    for l in six_char_diff:
        if l not in mapping.values():
            e = l
    mapping["e"] = e
    # mapping[e] = "e"

    # find g
    eight = get_of_len(input, 7)[0]
    g = ''
    for l in eight:
        if l not in mapping.values():
            g = l
    mapping["g"] = g
    # mapping[g] = "g"

    return mapping


# SEGMENTS
#   aaa
# b     c
# b     c
#   ddd
# e     f
# e     f
#   ggg

def calc_output(mapp, right_nums):
    mapping = {v: k for k, v in mapp.items()}

    def get_mapping(str):
        easy_nums = {
            2: 1,
            3: 7,
            4: 4,
            7: 8
        }
        ln = len(str)
        if ln in easy_nums:
            return easy_nums[ln]

        hard_nums = {
            'abcefg': 0,
            'acdeg': 2,
            'acdfg': 3,
            'abdfg': 5,
            'abdefg': 6,
            'abcdfg': 9
        }

        mapped_str = ''
        for l in str:
            lm = mapping[l]
            mapped_str += lm
        sms = ''.join(sorted(mapped_str))

        return hard_nums[sms]

    total = 0

    for num in right_nums:
        total *= 10
        total += get_mapping(num)

    return total


if __name__ == '__main__':
    # part1()
    print('====')
    part2()
