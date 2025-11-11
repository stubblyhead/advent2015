import re

if __name__ == '__main__':
    with open('testcase') as f:
        lines = f.readlines()

    molecule = lines.pop().strip()
    lines.pop()
    subs = []
    for l in lines:
        subs.append(tuple(l.strip().split(' => ')))
# H(?![a-z])
    new_molecules = {}

    for s in subs:
        tmp_mol = molecule
        tmp_mol.replace
