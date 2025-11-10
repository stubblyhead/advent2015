class Aunt:
    def __init__(self, name, things):
        self.name = name
        self.things = things

if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()
    
    aunts = set()
    for l in lines:
        l = l.split(',')
        tmp = l[0].split(': ')
        name = tmp[0]
        l[0] = tmp[1]+ ': ' + tmp[2]
        things = {}
        for thing in l:
            item,count = thing.split(':')
            things[item.strip()] = int(count)
        aunts.add(Aunt(name,things))
    aunts_deux = set(aunts)

    data = '''children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1'''.split('\n')
    detected = {}
    for d in data:
        item, count = d.split(':')
        detected[item] = int(count)
    
    for item in detected.keys():
        to_remove = set()
        for a in aunts:
            if item in a.things.keys() and detected[item] != a.things[item]:
                to_remove.add(a)
        aunts -= to_remove
        if len(aunts) == 1:
            last_aunt = aunts.pop()
            print(last_aunt.name)
            break

    for item in detected.keys():
        to_remove = set()
        for a in aunts_deux:
            if item in ['trees','cats']:
                if item in a.things.keys() and detected[item] >= a.things[item]:
                    to_remove.add(a)
            elif item in ['pomeranians','goldfish']:
                if item in a.things.keys() and detected[item] <= a.things[item]:
                    to_remove.add(a)
            else:
                if item in a.things.keys() and detected[item] != a.things[item]:
                    to_remove.add(a)
        aunts_deux -= to_remove
        if len(aunts_deux) == 1:
            last_aunt = aunts_deux.pop()
            print(last_aunt.name)
            break
        
    


        
