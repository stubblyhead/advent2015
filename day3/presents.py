from collections import defaultdict

if __name__ == '__main__':
    with open('input') as f:
        dirs = f.read().strip()

    houses = defaultdict(int)
    x,y=0,0
    houses[(x,y)] = 1
    for d in dirs:
        if d == '>':
            x += 1
        if d == '<':
            x -= 1
        if d == '^':
            y += 1
        if d == 'v':
            y -= 1
        houses[(x,y)] += 1
    print(len(houses.keys()))

    houses = defaultdict(int)
    
    s_x,s_y,r_x,r_y = 0,0,0,0
    houses[(s_x,s_y)] += 1
    for i in range(len(dirs)):
        d = dirs[i]
        if i%2:
            if d == '>':
                r_x += 1
            if d == '<':
                r_x -= 1
            if d == '^':
                r_y += 1
            if d == 'v':
                r_y -= 1
            houses[(r_x,r_y)] += 1
        else:
            if d == '>':
                s_x += 1
            if d == '<':
                s_x -= 1
            if d == '^':
                s_y += 1
            if d == 'v':
                s_y -= 1
            houses[(s_x,s_y)] += 1

    print(len(houses.keys()))