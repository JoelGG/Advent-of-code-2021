import numpy as np

# --- Day 1: Sonar Sweep - --

# You're minding your own business on a ship at sea when the overboard alarm
# goes off! You rush to see if you can help. Apparently, one of the Elves
# tripped and accidentally sent the sleigh keys flying into the ocean!

# Before you know it, you're inside a submarine the Elves keep ready for
# situations like this. It's covered in Christmas lights (because of course it
# is), and it even has an experimental antenna that should be able to track the
# keys if you can boost its signal strength high enough there's a little meter
# that indicates the antenna's signal strength by displaying 0-50 stars.

# Your instincts tell you that in order to save Christmas, you'll need to get
# all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each
# day in the Advent calendar the second puzzle is unlocked when you complete the
# first. Each puzzle grants one star. Good luck!

# As the submarine drops below the surface of the ocean, it automatically
# performs a sonar sweep of the nearby sea floor. On a small screen, the sonar
# sweep report(your puzzle input) appears: each line is a measurement of the sea
# floor depth as the sweep looks further and further away from the submarine.


def part_1(a): return np.sum((a[1:] - a[:-1]) > 0)


def part_2(a): return part_1(a[0:-2] + a[1:-1] + a[2:])


ds = np.fromfile("Day 1/depths.txt", sep=" ")
print(part_1(ds))
print(part_2(ds))
