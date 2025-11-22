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
    sublendict = {}
    sub_count = 0
    for i in subs:
        element_count = len(re.findall(r'[A-Z]', i[1]))
        if element_count not in sublendict.keys():
            sublendict[element_count] = [i]
        else:
            sublendict[element_count].append(i)
    
    for _ in range(500):
        if molecule == 'e':
            break
        made_sub = False
        for length in range(8,1,-1):
            if made_sub:
                break 
            if length in sublendict.keys():
                for sub in sublendict[length]:
                    long_mol = re.search(sub[1], molecule)
                    if long_mol:
                        molecule = molecule[:long_mol.span()[0]] + sub[0] + molecule[long_mol.span()[1]:]
                        sub_count += 1
                        made_sub = True
                        break
    print(sub_count)