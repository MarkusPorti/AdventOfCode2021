import math

from adventOfCode import get_data

lines = get_data(test=False)


def count_basins(x, y, n=None):
    if n is None:
        n = set()
    n.add((x, y))

    if x > 0:  # links Frei
        if field[y][x] < field[y][x - 1] < 9 and (x - 1, y) not in n:
            [n.add(x) for x in count_basins(x - 1, y, n)]
    if x < len(row) - 1:  # rechts Frei
        if field[y][x] < field[y][x + 1] < 9 and (x + 1, y) not in n:
            [n.add(x) for x in count_basins(x + 1, y, n)]
    if y > 0:  # oben Frei
        if field[y][x] < field[y - 1][x] < 9 and (x, y - 1) not in n:
            [n.add(x) for x in count_basins(x, y - 1, n)]
    if y < len(field) - 1:  # unten Frei
        if field[y][x] < field[y + 1][x] < 9 and (x, y + 1) not in n:
            [n.add(x) for x in count_basins(x, y + 1, n)]

    return n


field = [[int(x) for x in line] for line in lines]

sum_risk_levels = 0
basins = []
for y, row in enumerate(field):
    for x, value in enumerate(row):
        adjacent = []
        if x > 0:  # linker Rand
            adjacent.append(row[x - 1])
        if x < len(row) - 1:  # rechter Rand
            adjacent.append(row[x + 1])
        if y > 0:  # oberer Rand
            adjacent.append(field[y - 1][x])
        if y < len(field) - 1:  # unterer Rand
            adjacent.append(field[y + 1][x])

        if value < min(adjacent):
            # found low-point
            sum_risk_levels += 1 + value
            basins.append(len(count_basins(x, y)))


print(sum_risk_levels)

print(math.prod([x for x in sorted(basins, reverse=True)[:3]]))
