import re

if __name__ == '__main__':
    grid = [ [ 0 for _ in range(1000) ] for _ in range(1000) ]

    with open('input') as f:
        instructions = f.readlines()
    for i in instructions: 
        corners = re.findall(r'\d+,\d+', i)
        x1,y1 = corners[0].split(',')
        x2,y2 = corners[1].split(',')
        x1,x2,y1,y2 = int(x1),int(x2),int(y1),int(y2)

        if i.count('on'):
            # TODO on stuff
            for row in range(x1,x2+1):
                for col in range(y1,y2+1):
                    grid[row][col] = 1
        elif i.count('off'):
            # TODO off stuff
            for row in range(x1,x2+1):
                for col in range(y1,y2+1):
                    grid[row][col] = 0
        else:
            # TODO toggle stuff
            for row in range(x1,x2+1):
                for col in range(y1,y2+1):
                    grid[row][col] = (grid[row][col]+1)%2
        
    light_count = 0
    for row in grid:
        light_count += row.count(1)
    print(light_count)

    grid = [ [ 0 for _ in range(1000) ] for _ in range(1000) ]
    for i in instructions: 
        corners = re.findall(r'\d+,\d+', i)
        x1,y1 = corners[0].split(',')
        x2,y2 = corners[1].split(',')
        x1,x2,y1,y2 = int(x1),int(x2),int(y1),int(y2)

        if i.count('on'):
            # TODO on stuff
            for row in range(x1,x2+1):
                for col in range(y1,y2+1):
                    grid[row][col] += 1
        elif i.count('off'):
            # TODO off stuff
            for row in range(x1,x2+1):
                for col in range(y1,y2+1):
                    grid[row][col] -= 1
                    if grid[row][col] < 0:
                        grid[row][col] = 0
        else:
            # TODO toggle stuff
            for row in range(x1,x2+1):
                for col in range(y1,y2+1):
                    grid[row][col] += 2

    light_count = 0
    for row in grid:
        light_count += sum(row)
    print(light_count)