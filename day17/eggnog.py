from itertools import combinations

if __name__ == '__main__':
    with open('input') as f:
        cups = list(map(int, f.readlines()))

    valid = 0
    # need at least 4 cups and no more than 11 to get to 150
    for i in range(4,12):
        combos = combinations(cups, i)
        for i in combos:
            if sum(i) == 150:
                valid += 1

    print(valid)