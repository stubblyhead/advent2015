class Light:
    def __init__(self, lighted):
        self.lighted = int(lighted)
        self.toggle = False
    
    def __repr__(self):
        return str(int(self.lighted))

    def toggle(self):
        if self.toggle:
            self.lighted = not self.lighted
            self.toggle = False

class Grid:
    def __init__(self, grid):
        self.grid = grid

    def count_neighbors(self, row, col):
        count = 0
        for r in range(max([0,row-1]),min([len(self.grid)-1,row+1])+1):
            for c in range(max([0,col-1]),min([len(self.grid[row])-1,col+1])+1
                           ):
                if (r,c) == (row,col):
                    continue
                count += self.grid[r][c].lighted
        return count
            

if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()

    grid = []
    tr_table = str.maketrans('.#','01')
    for l in lines:
        l = l.translate(tr_table).strip()

        grid.append(list(map(Light,l)))

    grid = Grid(grid)

    print(grid.count_neighbors(10,10))