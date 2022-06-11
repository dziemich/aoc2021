file = '../inputs/day04.txt'
lines = []

for line in open(file):
    match = re.match(pattern, line)
    lines.append((match.group(1).replace('-', ''), int(match.group(2)), match.group(3)))
