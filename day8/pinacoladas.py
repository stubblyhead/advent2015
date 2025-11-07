if __name__ == '__main__':
    with open('input') as f:
        lines = list(map(str.strip,f.readlines()))

    
    string_length = 0
    code_length = 0

    for l in lines:
        code_length += len(l)
        l = l[1:-1]
        l = l.replace('\\\\','|')
        l = l.replace('\\"','`')
        this_len = len(l) - l.count('\\x')*3
        string_length += this_len

    print(code_length - string_length)

    encoded_length = 0
    for l in lines:
        this_len = len(l) + 4 # two add'l chars on either end
        l = l[1:-1]
        this_len = this_len + l.count('\\\\')*2 + l.count('\\"')*2 + l.count('\\x')
        encoded_length += this_len

    print(encoded_length - code_length)