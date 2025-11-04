if __name__ == '__main__':
    with open('input') as f:
        strings = f.readlines()

    nice = 0
    for s in strings:
        s = s.strip()
        # check for forbidden substrings
        bad_count = s.count('ab') + s.count('cd') + s.count('pq') + s.count('xy')
        if bad_count:
            continue
        # make sure there are enough vowels
        vowel_count = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')
        if vowel_count < 3:
            continue
        # look for double letters
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                nice += 1
                break

    print(nice)

    nice = 0
    for s in strings:
        s = s.strip()
        repeat_double = False
        for i in range(len(s)-1):
            if s.count(s[i]+s[i+1]) > 1:
                repeat_double = True
                break
        if repeat_double:
            for i in range(len(s)-2):
                if  s[i] == s[i+2]:
                    nice += 1
                    break
    print(nice)