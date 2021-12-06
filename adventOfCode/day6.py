from adventOfCode import get_data

lines = get_data(test=False)

fishes = [int(x) for x in lines[0].split(',')]

counts = [fishes.count(x) for x in range(9)]

for i in range(256):
    new_fishes = counts[0]
    for j in range(len(counts) - 1):
        counts[j] = counts[j+1]
    counts[6] += new_fishes
    counts[8] = new_fishes

print(sum(counts))
