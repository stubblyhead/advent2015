import re

if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()

    molecule = lines.pop().strip()
    lines.pop()
    subs = []
    for l in lines:
        subs.append(tuple(l.strip().split(' => ')))
    new_molecules = set()
    for s in subs:
        matches = re.finditer(f'{s[0]}(?![a-z])', molecule)
        for m in matches:
            start,end = m.span()
            new_molecules.add(molecule[:start]+s[1]+molecule[end:])
    
    print(len(new_molecules))
        
