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
                True
            elif i.count('off'):
                # TODO off stuff
                True
            else:
                # TODO toggle stuff
                True
            