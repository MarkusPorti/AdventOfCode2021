from adventOfCode import get_data
import time

lines = get_data(test=False)

times = time.time()
data = []
for line in lines:
    x1, y1, x2, y2 = [int(value) for value in line.split(' -> ') for value in value.split(',')]
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            data.append((x1, y))

    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            data.append((x, y1))

    if abs(x1 - x2) == abs(y1 - y2):  # vertical
        x_range = 1 if x1 < x2 else -1
        y_range = 1 if y1 < y2 else -1
        for x, y in zip(range(x1, x2 + x_range, x_range), range(y1, y2 + y_range, y_range)):
            data.append((x, y))
print("Calc points ({}): {:.10f} s".format(len(data), time.time() - times))

times = time.time()
# count duplicated points
elements = set()
result = set()
for i, item in enumerate(data):
    if item in elements:
        result.add(item)
    else:
        elements.add(item)
print("Get duplicated points: {:.10f} s".format(time.time() - times))

print(len(result))
