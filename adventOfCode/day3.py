from adventOfCode import get_data

lines = get_data(test=False)

vertical = []
for line in lines:
    for i, char in enumerate(line):
        if len(vertical) <= i:
            vertical.insert(i, char)
        else:
            vertical[i] += char

gamma, epsilon = "0b", "0b"
for bits in vertical:
    zeroes = bits.count('0')
    ones = bits.count('1')
    if ones > zeroes:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma * epsilon)


def find_rating(numbers, i=0, most_common=True):
    if len(numbers) == 1:
        return int(numbers[0], 2)

    ones, zeroes = [], []
    for number in numbers:
        if number[i] == '1':
            ones.append(number)
        else:
            zeroes.append(number)

    if most_common:
        if len(ones) >= len(zeroes):
            return find_rating(ones, i+1, most_common)
        else:
            return find_rating(zeroes, i+1, most_common)
    else:
        if len(ones) < len(zeroes):
            return find_rating(ones, i+1, most_common)
        else:
            return find_rating(zeroes, i+1, most_common)


oxygen = find_rating(lines, most_common=True)
c02 = find_rating(lines, most_common=False)
print(oxygen * c02)
