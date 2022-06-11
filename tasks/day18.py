file = '../inputs/day18.txt'

from math import floor, ceil


class Node:
    def __init__(self, val, left, right, prev, next):
        self.val = val
        self.left = left
        self.right = right
        self.prev = prev
        self.next = next


def parse(arr):
    left, right = arr
    l_node, r_node = None, None
    if not isinstance(left, list):
        l_node = Node(left, None, None, None, None)
    else:
        l_node = parse(left)
    if not isinstance(right, list):
        r_node = Node(right, None, None, None, None)
    else:
        r_node = parse(right)

    l_iter = l_node
    r_iter = r_node
    while l_iter.right is not None:
        l_iter = l_iter.right

    while r_iter.left is not None:
        r_iter = r_iter.left

    l_iter.next = r_iter
    r_iter.prev = l_iter

    return Node(None, l_node, r_node, None, None)


def print_root(root):
    if root.val is not None:
        return root.val
    l, r = None, None
    if root.left is not None:
        l = print_root(root.left)
    if root.right is not None:
        r = print_root(root.right)

    return [l, r]


def part1():
    with open(file) as f:
        exploded = False
        splitted = False

        def explode(node, level):
            # print("exploding")
            nonlocal exploded
            if node is None:
                return
            if exploded:
                return
            if level == 3 and node.val is None:
                if node.left.val is None or node.right.val is None:
                    if exploded:
                        return
                    exploded = True

                    if node.left.val is None:
                        curr_node = node.left
                        print("exploading:[" + str(curr_node.left.val) + "," + str(curr_node.right.val) + "]")
                        p = curr_node.left.prev
                        if p is not None:
                            p.val += curr_node.left.val
                        n = curr_node.right.next
                        if n is not None:
                            n.val += curr_node.right.val
                        curr_node.val = 0
                        curr_node.prev = p
                        if p is not None:
                            p.next = curr_node
                        curr_node.next = n
                        if n is not None:
                            n.prev = curr_node
                        curr_node.left = None
                        curr_node.right = None

                        return
                    elif node.right.val is None:
                        if exploded:
                            return
                        curr_node = node.right
                        print("exploading:[" + str(curr_node.left.val) + "," + str(curr_node.right.val) + "]")
                        p = curr_node.left.prev
                        if p is not None:
                            p.val += curr_node.left.val
                        n = curr_node.right.next
                        if n is not None:
                            n.val += curr_node.right.val
                        curr_node.val = 0
                        curr_node.prev = p
                        if p is not None:
                            p.next = curr_node
                        curr_node.next = n
                        if n is not None:
                            n.prev = curr_node
                        curr_node.left = None
                        curr_node.right = None
                        return
                return
            explode(node.left, level + 1)
            explode(node.right, level + 1)

        def split(node):
            nonlocal splitted
            if node is None:
                return
            if splitted:
                return
            if node.left is not None and node.left.val is not None and node.left.val >= 10:
                splitted = True
                print("spli")
                curr_node = node.left
                p = curr_node.prev
                n = curr_node.next

                l_node = Node(floor(curr_node.val / 2), None, None, None, None)
                r_node = Node(ceil(curr_node.val / 2), None, None, None, None)
                l_node.prev = p
                p.next = l_node
                l_node.next = r_node
                r_node.prev = l_node
                r_node.next = n
                n.prev = r_node

                curr_node.val = None
                curr_node.left = l_node
                curr_node.right = r_node
                curr_node.prev = None
                curr_node.next = None
                return

            elif node.right is not None and node.right.val is not None and node.right.val >= 10:
                splitted = True
                curr_node = node.right
                p = curr_node.prev
                n = curr_node.next

                l_node = Node(floor(curr_node.val / 2), None, None, None, None)
                r_node = Node(ceil(curr_node.val / 2), None, None, None, None)
                l_node.prev = p
                p.next = l_node
                l_node.next = r_node
                r_node.prev = l_node
                r_node.next = n
                n.prev = r_node

                curr_node.val = None
                curr_node.left = l_node
                curr_node.right = r_node
                curr_node.prev = None
                curr_node.next = None
                return
            split(node.left)
            split(node.right)

        def magn(node):
            # print("magn")
            if node.val is not None:
                return node.val

            if node.left is not None and node.right is not None:
                return 3 * magn(node.left) + 2 * magn(node.right)

        lines = f.read().split("\n")

        curr_root = parse(eval(lines[0]))

        for arr in lines[1:]:
            nroot = parse(eval(arr))
            root = Node(None, curr_root, nroot, None, None)

            l_iter = curr_root
            r_iter = nroot
            while l_iter.right is not None:
                l_iter = l_iter.right

            while r_iter.left is not None:
                r_iter = r_iter.left

            l_iter.next = r_iter
            r_iter.prev = l_iter

            explode(root, 0)
            split(root)
            while exploded or splitted:
                exploded = False
                splitted = False
                explode(root, 0)
                split(root)

            curr_root = root

        print(magn(curr_root))


if __name__ == '__main__':
    part1()
    # print('====')
    # part2()
