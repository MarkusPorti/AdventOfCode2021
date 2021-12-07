from adventOfCode import get_data

lines = get_data(test=False)

positions = [int(x) for x in lines[0].split(',')]

result = 1e15


def sum_of(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


for i in range(min(positions), max(positions) + 1):
    fuel = 0
    for pos in positions:
        fuel += sum_of(abs(pos - i))
    result = min(fuel, result)

print(result)
