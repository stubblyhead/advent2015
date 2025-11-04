from hashlib import md5

prefix = 'ckczppom'

num = 0
while True:
    num += 1
    input = prefix+str(num)
    hash = md5(bytes(input, 'utf-8'))
    if hash.hexdigest()[:5] == '00000':
        print(num)
        break

while True:
    num += 1
    input = prefix+str(num)
    hash = md5(bytes(input, 'utf-8'))
    if hash.hexdigest()[:6] == '000000':
        print(num)
        break