if __name__ == "__main__":

    with open('input') as f:
        prezzies = f.readlines()

    def format_present(present):
        dims = present.split('x')
        dims = list(map(int,dims))
        dims.sort()
        return dims
    
    prezzies = list(map(format_present, prezzies))

    paper = 0
    ribbon = 0
    for p in prezzies:
        (l,w,h) = p
        paper = paper + 2*l*w + 2*l*h + 2*w*h + l*w
        ribbon = ribbon + 2*(l+w) + l*w*h
    print(paper)
    print(ribbon)