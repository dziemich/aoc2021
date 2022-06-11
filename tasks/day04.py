class Board:
    def __init__(self, board):
        self.board = board
        self.called = []

    def call_num(self, num):
        self.called.append(num)

    def is_winner(self):
        for i in range(0, 5):
            is_win_v = True
            is_win_h = True
            for j in range(0, 5):
                if self.board[i][j] not in self.called:
                    is_win_h = False
                if self.board[j][i] not in self.called:
                    is_win_v = False
            if is_win_h or is_win_v:
                return True
        return False

    def calc_not_called(self):
        total = 0
        for i in range(0, 5):
            for j in range(0, 5):
                if self.board[i][j] not in self.called:
                    total += int(self.board[i][j])
        return total


file = '../inputs/day04.txt'


def part1():
    with open(file) as f:
        raw_lines = f.read().split("\n")

        input = list(map(lambda n: int(n), raw_lines[0].split(",")))
        boards = []

        for i in range(2, len(raw_lines), 6):
            elems = raw_lines[i:i + 5]
            board = list(map(lambda l: list(map(lambda s: int(s), l.split())), elems))

            boards.append(Board(board))

        for num in input:
            for b in boards:
                b.call_num(num)
                if b.is_winner():
                    print(b.calc_not_called() * num)
                    return


def part2():
    with open(file) as f:
        raw_lines = f.read().split("\n")

        input = list(map(lambda n: int(n), raw_lines[0].split(",")))
        boards = []

        for i in range(2, len(raw_lines), 6):
            elems = raw_lines[i:i + 5]
            board = list(map(lambda l: list(map(lambda s: int(s), l.split())), elems))
            boards.append(Board(board))

        for num in input:
            for b in boards:
                b.call_num(num)
            for b in boards:
                if b.is_winner():
                    if len(boards) == 1:
                        print(b.calc_not_called() * num)
                        return
                    else:
                        boards.remove(b)


# part 1
if __name__ == '__main__':
    part1()
    print('====')
    part2()
