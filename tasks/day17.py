def sim_step(pos, vel):
    newx = pos[0] + vel[0]
    newy = pos[1] + vel[1]
    nvx = vel[0]
    if nvx < 0:
        nvx += 1
    elif nvx > 0:
        nvx -= 1
    nvy = vel[1] - 1

    return (newx, newy), (nvx, nvy)


def is_within(pos, x_area, y_area):
    return x_area[0] <= pos[0] <= x_area[1] and y_area[0] <= pos[1] <= y_area[1]


def project(init, vel, x_area, y_area):
    # print("projecting for vel " + str(vel) + " at " + str(init))
    my = 0
    pos = init
    while pos[0] <= x_area[1] and pos[1] >= y_area[0]:
        npos, nvel = sim_step(pos, vel)
        my = max(my, npos[1])

        if is_within(npos, x_area, y_area):
            return my
        pos = npos
        vel = nvel
    return -1


def part1():
    x_area = (25, 67)
    y_area = (-260, -200)

    my = 0

    for x in range(0, 50):
        for y in range(0, 300):
            p = project((0, 0), (x, y), x_area, y_area)
            my = max(my, p)

    print(my)


def part2():
    x_area = (25, 67)
    y_area = (-260, -200)
    sum = 0
    for x in range(-100, 100):
        for y in range(-300, 300):
            p = project((0, 0), (x, y), x_area, y_area)
            if p != -1:
                sum += 1

    print(sum)


if __name__ == '__main__':
    # part1()
    print('====')
    part2()
