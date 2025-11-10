from itertools import combinations

if __name__ == '__main__':
    with open('input') as f:
        cups = list(map(int, f.readlines()))

    valid = { i: 0 for i in range(4,12) }
    # need at least 4 cups and no more than 11 to get to 150
    for i in range(4,12):
        combos = combinations(cups, i)
        for j in combos:
            if sum(j) == 150:
                valid[i] += 1

    print(sum(valid.values()))
    for k,v in valid.items():
        if v > 0:
            print(v)
            break