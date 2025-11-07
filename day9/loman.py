from itertools import permutations

if __name__ == '__main__':
    with open('input') as f:
        distances = list(map(str.strip, f.readlines()))

    dist_dict = {}
    for d in distances:
        d = d.split()
        if d[0] not in dist_dict.keys():
            dist_dict[d[0]] = {}
        dist_dict[d[0]][d[2]] = int(d[-1])
        if d[2] not in dist_dict.keys():
            dist_dict[d[2]] = {}
        dist_dict[d[2]][d[0]] = int(d[-1])

    total_dists = []
    for p in permutations(dist_dict.keys()):
        this_total = 0
        for i in range(len(p) -1):
            this_total += dist_dict[p[i]][p[i+1]]
        total_dists.append(this_total)
    print(min(total_dists),max(total_dists))
        
        