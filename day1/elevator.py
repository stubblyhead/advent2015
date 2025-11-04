if __name__ == '__main__':

    with open('input') as f:
        inst = f.read()
        print(inst.count('(') - inst.count(')'))

    floor = 0
    for i in range(len(inst)):
        if inst[i] == '(':
            floor += 1
        elif inst[i] == ')':
            floor -= 1
            if floor < 0:
                print(i+1)
                break   
        else:
            print(f"unexpected char, found {inst[i]}")