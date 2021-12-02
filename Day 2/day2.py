import numpy as np


def part_1(l, v):
    vt = np.concatenate((v[l == "up"] * -1, v[l == "down"])).sum()
    hz = v[l == "forward"].sum()
    return vt * hz


# presented on multiple lines for clarity, could be combined into a single statement
def part_2(l, v):
    # all vertical values, adjusted for up being negative
    verts = ((l == "up") * -1 * v) + ((l == "down") * v)
    # aim over time
    aim = np.cumsum(verts)
    # all horizontal values
    horz = (l == "forward") * v
    # position adjusted for aim
    adjusted_position = (aim * horz).sum()
    # depth adjusted for aim
    adjusted_depth = horz.sum()
    return adjusted_position * adjusted_depth

# basic iterative solution for sanity check


def part_2_iterative(l, v):
    horizontal = 0
    vertical = 0
    aim = 0
    for i in range(0, len(v)):
        label = l[i]
        scalar = v[i]
        if (label == "up"):
            aim = np.abs(aim - scalar)
        elif (label == "down"):
            aim = aim + scalar
        else:
            horizontal += scalar
            vertical += scalar * aim
    return horizontal * vertical


labels = np.genfromtxt("Day 2/commands.txt", usecols=0,
                       dtype=None, encoding=None)
values = np.genfromtxt("Day 2/commands.txt", usecols=1)

p1 = part_1(labels, values)
p2 = part_2(labels, values)
p2i = part_2_iterative(labels, values)

print(p1)
print(p2)
