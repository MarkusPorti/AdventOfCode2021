def get_data(test=False) -> list[str]:
    with open('test.data' if test else 'input.data') as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]
