from adventOfCode import get_data

lines = get_data(test=False)

field = [[int(x) for x in line] for line in lines]
count_flashes = 0


def check_flash(x, y):
    count = 0
    if field[x][y] > 9:
        field[x][y] = 0
        count += 1
        for v in range(-1, 2):
            for h in range(-1, 2):
                if x + v < 0 or x + v >= len(field):
                    continue
                if y + h < 0 or y + h >= len(field[x]):
                    continue
                if field[x + v][y + h] > 0:
                    field[x + v][y + h] += 1
                    count += check_flash(x + v, y + h)
    return count


all_flash = False
step = 0
while not all_flash:
    field = [[x + 1 for x in line] for line in field]

    for i in range(len(field)):
        for j in range(len(field[i])):
            count_flashes += check_flash(i, j)
    all_flash = all([x == 0 for line in field for x in line])
    step += 1

print(count_flashes)
print(step)
