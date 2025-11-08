import itertools

def format_string(s):
    words = s.split()
    words[3] = int(words[3])
    if words.count('lose'):
        words[3] *= -1
    return [words[0],words[3],words[-1][:-1]]

def get_happiness(guests,order):
    guest_count = len(order)
    this_happy = 0
    for i in range(guest_count):
        r = guests[order[i]][order[(i+1)%guest_count]]
        l = guests[order[i]][order[(i-1)%guest_count]]
        this_happy += (r+l)
    return this_happy

if __name__ == '__main__':
    with open('input') as f:
        rules = list(map(format_string,f.readlines()))

        guests = {}
        for r in rules:
            if r[0] not in guests.keys():
                guests[r[0]] = {}
            guests[r[0]][r[2]] = r[1]
        max_happy = -1000 
        guest_perms = itertools.permutations(guests.keys())
        guest_count = len(guests.keys())
        for p in guest_perms:
            this_happy = get_happiness(guests, p)
            
            max_happy = max([max_happy,this_happy])
        
        print(max_happy)

        guests['me'] = {}
        for g in guests.keys():
            if g == 'me':
                continue
            guests['me'][g] = 0
            guests[g]['me'] = 0

        guest_perms = itertools.permutations(guests.keys())
        guest_count = len(guests.keys())
        max_happy = 0
        for p in guest_perms:
            this_happy = get_happiness(guests, p)
            
            max_happy = max([max_happy,this_happy])
        
        print(max_happy)

