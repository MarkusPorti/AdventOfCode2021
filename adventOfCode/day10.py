from adventOfCode import get_data

lines = get_data(test=False)

score = 0
for line in lines:
    last_open = []
    for c in line:
        if c in "([{<":
            last_open.append(c)
        else:
            open = last_open.pop()
            if c == ")" and open != "(":
                score += 3
                break
            if c == "]" and open != "[":
                score += 57
                break
            if c == "}" and open != "{":
                score += 1197
                break
            if c == ">" and open != "<":
                score += 25137
                break

print(score)

# Part Two
scores = []
for line in lines:
    last_open = []

    for c in line:
        if c in "([{<":
            last_open.append(c)
        else:
            if len(last_open) == 0:
                break
            open = last_open.pop()
            if c == ")" and open != "(" or c == "]" and open != "[" or \
                    c == "}" and open != "{" or c == ">" and open != "<":
                last_open.clear()
                break

    if len(last_open) > 0:
        score = 0
        for open in reversed(last_open):
            if open in "([{<":
                score = score * 5 + "([{<".index(open) + 1
        scores.append(score)

print(sorted(scores)[len(scores) // 2])
