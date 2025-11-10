if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()

    grid = []
    for l in lines:
        tr_table = str.maketrans('.#','01')
        l = l.translate(tr_table).strip()

        grid.append(list(map(int,l)))

    for g in grid:
        print(g)