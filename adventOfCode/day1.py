from adventOfCode import get_data

lines = get_data(test=False)


counter = 0
last_line = None
for i, line in enumerate(lines):
    if i > len(lines) - 3:
        break
    sum = line + lines[i+1] + lines[i+2]
    if last_line is not None and sum > last_line:
        counter += 1
    last_line = sum

print(counter)
