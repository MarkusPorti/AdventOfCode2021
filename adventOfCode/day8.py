from adventOfCode import get_data

lines = get_data(test=False)

#  aaaa
# b    c
# b    c
#  dddd
# e    f
# e    f
#  gggg

sum_outputs = 0
for line in lines:
    inputs = [set(value) for value in line.split(' | ')[0].split(' ')]
    inputs.sort(key=len)
    numbers = [set() for x in range(10)]

    for value in inputs:
        if len(value) == 2:  # -> "1"
            numbers[1] = value
        if len(value) == 3:  # -> "7"
            numbers[7] = value
        if len(value) == 4:  # -> "4"
            numbers[4] = value
        if len(value) == 5:
            if len(value - numbers[7]) == 2:  # wenn 5-stellig minus 7 = 2 dann ists die "3"
                numbers[3] = value
        if len(value) == 6:
            if len(value - numbers[1]) == 5:  # wenn 6-stellig minus 1 = 5 dann ists die "6"
                numbers[6] = value
            elif len(value - numbers[4]) == 2:  # wenn 6-stellig minus 4 = 2 dann ists die "9"
                numbers[9] = value
        if len(value) == 7:  # -> "8"
            numbers[8] = value
    # Zweiter durchlauf weil Reihenfolge variieren kann
    for value in inputs:
        if len(value) == 5:
            if len(value - numbers[4]) == 2 and len(value - numbers[7]) != 2:
                # wenn 5-stellig minus 4 = 2 dann ists die "5"
                numbers[5] = value
            elif len(value - numbers[4]) == 3:  # wenn 5-stellig minus 4 = 3 dann ists die "2"
                numbers[2] = value
        if len(value) == 6:
            if len(value - numbers[4]) == 3 and len(value - numbers[1]) != 5:
                # wenn 6-stellig minus 4 = 3 dann ists die "0"
                numbers[0] = value

    number = ""
    outputs = [set(value) for value in line.split(' | ')[1].split(' ')]
    for output in outputs:
        number += str(numbers.index(output))
    print(number)
    sum_outputs += int(number)

print(sum_outputs)
