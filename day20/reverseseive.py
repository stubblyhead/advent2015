from functools import reduce

def get_factors(num):
    return set(reduce(
        list.__add__,
        ([i, num//i] for i in range(1,int(n**0.5)+1) if n%i ==0 )))

    
    


if __name__ == '__main__':
    # HCN = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, \
    #        720, 840, 1260, 1680, 2520, 5040, 7560, 10080, 15120, \
    #        20160, 25200, 27720, 45360, 50400, 55440, 83160, 110880, \
    #        166320, 221760, 277200, 332640, 498960, 554400, 665280, \
    #        720720, 1081080, 1441440, 2162160]
    
    target = 34_000_000

    # houses get 10x the product of unique prime factors, so i need the
    # lowest number with product of unique prime factors less than 
    # 34000000 / 10 = 3400000 = 3.4 million

    numbers = list(range(720720,1081080))
    
    for n in numbers:
        if sum(get_factors(n))*10 >= target:
            print(n)
            break