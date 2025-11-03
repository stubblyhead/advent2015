if __name__ == '__main__':

    with open('input') as f:
        inst = f.read()
        print(inst.count('(') - inst.count(')'))
