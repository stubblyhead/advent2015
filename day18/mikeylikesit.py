class Light:
    def __init__(self, lighted):
        self.lighted = lighted
        self.toggle = False
    
    def __repr__(self):
        return str(int(self.lighted))

    def toggle(self):
        if self.toggle:
            self.lighted = not self.lighted
            self.toggle = False

class Grid:
    def __init__(self, grid):
        self.grid = g

    def count_neighbors(grid, row, col):
        count = 0
        for r in range(max([0,row-1]),min([len(g)-1,row+1])):
            for c in range(max([0,col-1]),min([len(g[row])-1,col+1])):
                if (r,c) == (row,col):
                    continue
                count += g[r][c].lighted
            

if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()

    grid = []
    for l in lines:
        tr_table = str.maketrans('.#','01')
        l = l.translate(tr_table).strip()

        grid.append(list(map(Light,l)))

    for g in grid:
        print(g)