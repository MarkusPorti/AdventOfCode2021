from adventOfCode import get_data

lines = get_data(test=False)

horizontal, depth, aim = 0, 0, 0

for line in lines:
    command = line.split(" ")
    x = int(command[1])
    if command[0] == "forward":
        horizontal += x
        depth += (aim * x)
    elif command[0] == "up":
        aim -= x
    elif command[0] == "down":
        aim += x

print(horizontal * depth)
