class Light:
    def __init__(self, lighted):
        self.lighted = int(lighted)
        self.toggle = False
    
    def __repr__(self):
        if self.lighted:
            return '#'
        else:
            return '.'

    def do_toggle(self):
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

    def toggle_all(self):
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                self.grid[r][c].do_toggle()

    def __repr__(self):
        out_str = ''
        for r in self.grid:
            for l in r:
                out_str += l.__repr__()
            out_str += '\n'
        return out_str

            

if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()

    grid = []
    tr_table = str.maketrans('.#','01')
    for l in lines:
        l = l.translate(tr_table).strip()

        grid.append(list(map(Light,l)))

    grid = Grid(grid)
    print(grid)
    for _ in range(100
                   ):
        for r in range(len(grid.grid)):
            for c in range(len(grid.grid[r])):
                neighbors = grid.count_neighbors(r,c)
                if grid.grid[r][c].lighted and neighbors not in [2,3]:
                    grid.grid[r][c].toggle = True
                elif not grid.grid[r][c].lighted and neighbors == 3:
                    grid.grid[r][c].toggle = True
        grid.toggle_all()


    on_lights = 0
    for r in grid.grid:
        for l in r:
            on_lights += l.lighted

    print(on_lights)