from re import findall,search

def get_next(letters):
    i = len(letters)-1
    letters = list(letters)
    while i >= 0:
        if letters[i] == 'z':
            letters[i] = 'a'
            i -= 1
        else:
            if letters[i] in [ 'h', 'k', 'n' ]:
                inc_amount = 2    
            else: 
                inc_amount = 1
            letters[i] = chr(ord(letters[i])+inc_amount)
            return ''.join(letters)

def validate_password(pw):
    if len(findall(r'(\w)\1',pw)) < 2:
        return False
    if not search(r'abc|bcd|cde|def|efg|fgh|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz',pw):
        return False
    return True

if __name__ == '__main__':
    letters = 'vzbxkghb'
    is_valid = False
    while not is_valid:
        letters = get_next(letters)
        is_valid = validate_password(letters)
    print(letters)
    is_valid = False
    while not is_valid:
        letters = get_next(letters)
        is_valid = validate_password(letters)
    print(letters)
   