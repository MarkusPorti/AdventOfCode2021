from adventOfCode import get_data

lines = get_data(test=False)

numbers = [int(x) for x in lines[0].split(',')]

boards = []
board = []
for i in range(2, len(lines)):
    if not lines[i]:
        # save one board
        boards.append(board)
        board = []
    else:
        board.append([[int(x), False] for x in lines[i].split()])
boards.append(board)


def mark_number(board: list[list[list]], number: int):
    for row in board:
        for x in row:
            if x[0] == number:
                x[1] = True


def check_winner(board: list[list[list]]):
    # check rows
    for row in board:
        won = True
        for x in row:
            if not x[1]:
                won = False
                break
        if won:
            return True
    # check columns
    for c in range(len(board[0])):
        won = True
        for r in range(len(board)):
            if not board[r][c][1]:
                won = False
                break
        if won:
            return True
    return False


def calc_score(board: list[list[list]], number):
    sum = 0
    for row in board:
        for x in row:
            if not x[1]:
                sum += x[0]
    return sum * number


def play_bingo():
    for number in numbers:
        for board in list(boards):
            mark_number(board, number)
            if check_winner(board):
                last_won = calc_score(board, number)
                boards.remove(board)
                if len(boards) == 0:
                    return last_won
    return 0


score = play_bingo()
print(score)
